"""Check the deliverable offline, without executing or training notebook models.

Install the root requirements first. Run from any working directory.
"""
import ast
import csv
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
from urllib.parse import unquote, urlsplit
import zipfile

import nbformat
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
TUTORIALS = (
    ('Tutorial_1_LV_Vol_Estimation', 'Tutorial_1_LV_Voltage_Estimation.ipynb', 'LV'),
    ('Tutorial_2_MV_Effects_Reference_Voltage', 'Tutorial_2_MV_Effects_Reference_Voltage.ipynb', 'MV'),
)
IGNORED = {'.git', '.venv', 'venv', 'node_modules'}
CACHES = {'__pycache__', '.ipynb_checkpoints', '.pytest_cache'}
# Negative checks for obsolete presentation labels, not required artifacts.
PACKAGING = re.compile(
    r'(?i:\boverleaf\b|\benglish\b|\banswers?\b|\beditions?\b|'
    r'\bversions?\b|\brevisions?\b)|(?<![\w])v\d+(?:[._]\d+)*(?![\w])|版本'
)
BAD_FILENAME = re.compile(r'(?i)overleaf|answers?|(?:^|[_ .-])v(?:ersion)?[_ .-]?\d+')
PERSONAL_PATH = re.compile(r'(?i)[a-z]:[\\/]+Users[\\/]|/(?:Users|home)/[^/\s]+/')
LINK = re.compile(r'!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+["\'][^"\']*["\'])?\)')
counts = {'links': 0, 'readme_links': 0, 'code_cells': 0, 'pdf_pages': 0, 'exercise_rows': 0}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_path(path):
    """Preserve spelling while normalizing '..', including on Windows."""
    relative = Path(os.path.abspath(path)).relative_to(ROOT)
    current = ROOT
    for part in relative.parts:
        require(current.is_dir(), f'Not a directory: {current}')
        require(part in {entry.name for entry in current.iterdir()},
                f'Missing or wrong-case path: {relative.as_posix()}')
        current /= part
    require(current.exists(), f'Missing path: {relative.as_posix()}')
    return current


def clean_markdown(text):
    return re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=\s]+', '', text)


def check_prose(text, location):
    match = PACKAGING.search(text)
    require(match is None, f'Obsolete presentation label in {location}: {match.group() if match else ""}')
    require(not PERSONAL_PATH.search(text), f'Personal machine path in {location}')


def check_links(text, parent, readme=False):
    targets = LINK.findall(text)
    targets += re.findall(r'<(?:img|a)\b[^>]*(?:src|href)=["\']([^"\']+)', text)
    targets += re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', text, flags=re.MULTILINE)
    definitions = set(re.findall(r'^\s*\[([^\]]+)\]:', text, flags=re.MULTILINE))
    for label, reference in re.findall(r'\[([^\]]+)\]\[([^\]]*)\]', text):
        require((reference or label) in definitions, f'Undefined link reference: {reference or label}')
    for target in targets:
        parsed = urlsplit(target.strip('<>'))
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        check_path(parent / unquote(parsed.path))
        counts['links'] += 1
        counts['readme_links'] += int(readme)


def check_zip(path, expected):
    with zipfile.ZipFile(path) as package:
        names = package.namelist()
        require(len(names) == len(set(names)), f'Duplicate entries: {path.name}')
        require(package.testzip() is None, f'Corrupt ZIP: {path.name}')
        require(set(names) == set(expected), f'Unexpected ZIP layout: {path.name}')
        for name, source in expected.items():
            member = PurePosixPath(name)
            require(not member.is_absolute() and '..' not in member.parts and '\\' not in name,
                    f'Unsafe ZIP entry: {name}')
            check_path(source)
            require(package.read(name) == source.read_bytes(), f'ZIP/local data mismatch: {name}')


def check_settings(value, location):
    if isinstance(value, dict):
        for key, item in value.items():
            require(not re.search(r'(?i)version|environment', key), f'Unnecessary runtime field in {location}: {key}')
            check_settings(item, location)
    elif isinstance(value, list):
        for item in value:
            check_settings(item, location)
    elif isinstance(value, str):
        require(not PERSONAL_PATH.search(value), f'Personal path in {location}')


def check_notebook(tutorial, name, number):
    book = nbformat.read(tutorial / name, as_version=4)
    nbformat.validate(book)
    cut = next(i for i, cell in enumerate(book.cells)
               if cell.cell_type == 'markdown' and cell.source.startswith('## 3.'))
    execution_counts, todo_count = [], 0
    source_parts = []
    for index, cell in enumerate(book.cells):
        source_parts.append(cell.source)
        location = f'{name}, cell {index}'
        if cell.cell_type == 'markdown':
            prose = clean_markdown(cell.source)
            check_prose(prose, location)
            check_links(prose, tutorial)
        elif cell.cell_type == 'code':
            ast.parse(cell.source, filename=location)
            counts['code_cells'] += 1
            if index < cut:
                execution_counts.append(cell.execution_count)
            else:
                require(cell.execution_count is None and not cell.outputs, f'Executed student workspace: {location}')
                require('TODO' in cell.source, f'Missing student TODO: {location}')
                todo_count += 1
            for output in cell.outputs:
                require(output.output_type != 'error', f'Saved error: {location}')
                require(not (output.output_type == 'stream' and output.name == 'stderr'), f'Saved stderr: {location}')
                visible = output.get('text', '') + '\n'.join(
                    str(value) for mime, value in output.get('data', {}).items() if mime.startswith('text/')
                )
                require(not PERSONAL_PATH.search(visible), f'Personal path in output: {location}')
                require(not re.search(r'(?i)\b(?:keras|tensorflow|python)\s*[:=]?\s*\d+\.\d+|no gpu|cuda error', visible),
                        f'Runtime noise: {location}')
    require(execution_counts == list(range(1, len(execution_counts) + 1)), f'Non-contiguous main execution: {name}')
    require(todo_count == 7, f'Expected seven student TODOs: {name}')
    source = '\n'.join(source_parts)
    require(f'Tutorial_{number}_Colab_Data.zip' in source, f'Wrong Colab archive: {name}')
    require(f'added_path = "Tutorial_{number}"' in source, f'Wrong Colab folder: {name}')
    require('RUN_MODE = "quick"' in source, f'Saved tutorial is not quick mode: {name}')
    record = book.metadata.get('tutorial_results', {})
    require(record.get('mode') == 'quick' and len(record.get('files', {})) == 5, f'Missing result integrity record: {name}')
    for relative, sha256 in record['files'].items():
        file = check_path(tutorial / relative)
        require(digest(file) == sha256, f'Notebook/result file mismatch: {relative}')
    return len(execution_counts)


def rows(path):
    with path.open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def check_exercise_tables(tutorial, tex, number):
    result = tutorial / 'results/exercises'
    configurations = rows(result / 'exercise_configurations.csv')
    seeds = rows(result / 'exercise_seeds.csv')
    customers = rows(result / 'exercise_customer_rmse.csv')
    metrics = rows(result / 'exercise_test_metrics.csv')
    settings = json.loads((result / 'exercise_settings.json').read_text(encoding='utf-8'))
    require(len(customers) == 31, 'Expected all 31 customer errors')
    require([int(row['Customer']) for row in customers] == list(range(1, 32)), 'Customer order mismatch')
    if number == 1:
        config_columns = ['hidden_neurons', 'activation', 'epochs', 'RMSE_kfold', 'RMSE_std']
        seed_columns = ['seed', 'RMSE_kfold', 'RMSE_std']
    else:
        config_columns = ['hidden_neurons', 'PQ_only_RMSE_kfold', 'PQ_only_RMSE_std',
                          'PQ_plus_Vref_RMSE_kfold', 'PQ_plus_Vref_RMSE_std', 'joint_RMSE_kfold']
        seed_columns = ['seed', 'PQ_only_RMSE_kfold', 'PQ_plus_Vref_RMSE_kfold', 'joint_RMSE_kfold']
    table_rows = {re.sub(r'\s+', ' ', line.strip()) for line in tex.splitlines() if '&' in line}
    for dataset, columns in ((configurations, config_columns), (seeds, seed_columns),
                             (customers, list(customers[0])), (metrics, list(metrics[0]))):
        for row in dataset:
            cells = []
            for column in columns:
                value = row[column]
                if column not in {'hidden_neurons', 'epochs', 'seed', 'Customer', 'activation', 'Metric', 'Model'}:
                    value = f'{float(value):.6f}'
                cells.append(value)
            expected = ' & '.join(cells) + r' \\'
            require(expected in table_rows, f'LaTeX/CSV row mismatch: {tutorial.name}: {expected}')
            counts['exercise_rows'] += 1
    score = 'RMSE_kfold' if number == 1 else 'joint_RMSE_kfold'
    best = min(configurations, key=lambda row: float(row[score]))
    for key, value in settings['configuration'].items():
        require(str(value) == best[key] or (key != 'activation' and float(value) == float(best[key])),
                f'Exercise configuration/JSON mismatch: {key}')
    selected_seed = int(min(seeds, key=lambda row: float(row[score]))['seed'])
    require(selected_seed == settings['selected_seed'], 'Exercise seed/JSON mismatch')
    require(f'Selected seed: {selected_seed}.' in tex, 'LaTeX/JSON seed mismatch')
    require(settings['folds'] == 3 and settings['training_fits'] == (22 if number == 1 else 32), 'Exercise fit count mismatch')


def check_solution(tutorial, name, number):
    stem = f'Tutorial_{number}_Exercise_Solutions'
    source, pdf = check_path(tutorial / (stem + '.tex')), check_path(tutorial / (stem + '.pdf'))
    tex = source.read_text(encoding='utf-8')
    check_prose(tex, source.name)
    require(name in tex, f'Solution source names the wrong notebook: {source.name}')
    listings = re.findall(r'\\begin\{lstlisting\}(?:\[[^\]]*\])?\s*\n(.*?)\\end\{lstlisting\}', tex, re.DOTALL)
    require(len(listings) == 7, f'Expected seven complete exercise listings: {source.name}')
    for index, listing in enumerate(listings, 1):
        ast.parse(listing, filename=f'{source.name}:listing {index}')
    assets = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', tex)
    for asset in assets:
        require(asset.startswith('assets/'), f'Unstable document asset: {asset}')
        check_path(tutorial / asset)
    record = json.loads(check_path(tutorial / 'assets/solutions_build.json').read_text(encoding='utf-8'))
    require(record['source'] == source.name and record['pdf'] == pdf.name, 'PDF build filenames differ')
    require(record['source_sha256'] == digest(source) and record['pdf_sha256'] == digest(pdf),
            f'Source/PDF changed since build: {stem}')
    require(set(record['assets']) == set(assets), f'PDF build assets differ: {stem}')
    for asset, expected_hash in record['assets'].items():
        require(digest(tutorial / asset) == expected_hash, f'PDF asset changed since build: {asset}')
    reader = PdfReader(pdf)
    require(not reader.is_encrypted and len(reader.pages) > 0, f'Unreadable PDF: {pdf.name}')
    check_prose(str(reader.metadata.title or ''), f'{pdf.name} title metadata')
    title = ('LV Voltage Estimation' if number == 1 else 'MV Effects and Reference Voltage')
    require(reader.metadata.title == f'Tutorial {number}: {title} - Exercise Solutions', f'Unexpected PDF title: {pdf.name}')
    extracted = []
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ''
        require(len(text.strip()) > 20, f'Empty PDF page: {pdf.name}:{page_number}')
        check_prose(text, f'{pdf.name}:{page_number}')
        extracted.append(text)
    complete = '\n'.join(extracted)
    for exercise in ('E1.1', 'E1.2', 'E1.3', 'E2.1', 'E2.2', 'E2.3', 'E2.4'):
        require(exercise in complete, f'Missing exercise in PDF: {exercise}')
    counts['pdf_pages'] += len(reader.pages)
    check_exercise_tables(tutorial, tex, number)
    return len(reader.pages)


def main():
    files = []
    for path in ROOT.rglob('*'):
        relative = path.relative_to(ROOT)
        if IGNORED.intersection(relative.parts):
            continue
        require(not CACHES.intersection(relative.parts), f'Generated cache in deliverable: {relative}')
        if path.is_file():
            files.append(path)
            require(not BAD_FILENAME.search(path.name), f'Obsolete filename: {relative}')
            require(path.stat().st_size < 100 * 1024 * 1024, f'File exceeds normal GitHub limit: {relative}')
            require(path.suffix not in {'.pyc', '.aux', '.log', '.out', '.xdv', '.tmp'}, f'Temporary file: {relative}')
            if path.suffix == '.md':
                text = path.read_text(encoding='utf-8')
                check_prose(text, relative)
                check_links(text, path.parent, readme=path.name == 'README.md')
            if path.suffix == '.json':
                check_settings(json.loads(path.read_text(encoding='utf-8')), relative)
            if path.name.startswith('requirements') and path.suffix == '.txt':
                for line in path.read_text(encoding='utf-8').splitlines():
                    if line.startswith('-r '):
                        check_path(path.parent / line[3:].strip())
    notebooks = {path.relative_to(ROOT).as_posix() for path in files if path.suffix == '.ipynb'}
    require(notebooks == {f'{folder}/{name}' for folder, name, _ in TUTORIALS}, 'Expected exactly two student notebooks')
    headings = []
    for number, (folder, name, prefix) in enumerate(TUTORIALS, 1):
        tutorial = ROOT / folder
        readme = (tutorial / 'README.md').read_text(encoding='utf-8')
        headings.append(re.findall(r'^## .+$', readme, re.MULTILINE))
        for label in ('Student notebook', 'Colab data ZIP', 'Local dependencies',
                      'Exercise solutions (LaTeX)', 'Exercise solutions (PDF)'):
            require(f'[{label}]' in readme, f'Missing resource label: {folder}: {label}')
        main_cells = check_notebook(tutorial, name, number)
        pages = check_solution(tutorial, name, number)
        settings = json.loads((tutorial / f'results/tutorial/quick/{prefix}_keras_run_settings.json').read_text(encoding='utf-8'))
        require(settings['mode'] == 'quick' and settings['training_runs'] == (79 if number == 1 else 68), 'Main fit budget mismatch')
        if number == 1:
            expected = {f'data/{split}/{kind}.pkl': tutorial / f'synthentic_data_5_min_LV/{split}/{kind}.pkl'
                        for split in ('training', 'test') for kind in ('PQ', 'V')}
            expected['LVnetwork-topology.png'] = tutorial / 'LVnetwork-topology.png'
        else:
            expected = {f'data/synthentic_data_5_min_mv_secondary/{split}/{kind}.pkl':
                        tutorial / f'synthentic_data_5_min_mv_secondary/{split}/{kind}.pkl'
                        for split in ('training_tx', 'test_tx') for kind in ('PQ', 'V', 'V_secondary')}
            expected.update({f'network/{filename}': tutorial / 'network' / filename
                             for filename in ('customer_topology.csv', 'MG1_topology.png')})
        check_zip(tutorial / f'Tutorial_{number}_Colab_Data.zip', expected)
        print(f'PASS Tutorial {number}: {main_cells} sequential main cells; 7 unexecuted TODOs; {pages} PDF pages; Colab ZIP matches local data.')
    require(headings[0] == headings[1], 'Tutorial README section order differs')
    print(f'PASS: 2 notebooks; {counts["code_cells"]} Python cells; 2 LaTeX sources and rebuilt PDFs; {counts["exercise_rows"]} matching exercise table rows.')
    print(f'PASS: {counts["links"]} local Markdown links ({counts["readme_links"]} in the three READMEs); 0 broken links; exact filename case checked.')
    print('PASS: no obsolete presentation labels, personal paths or generated caches in the checked deliverable content.')


if __name__ == '__main__':
    main()
