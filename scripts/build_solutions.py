"""Compile the solution PDFs and update their source/asset integrity records."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = {
    1: 'Tutorial_1_LV_Vol_Estimation',
    2: 'Tutorial_2_MV_Effects_Reference_Voltage',
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tutorial', type=int, choices=FOLDERS, help='Build just one tutorial.')
    parser.add_argument('--compiler', default='tectonic', help='Tectonic executable name or path.')
    args = parser.parse_args()
    compiler = shutil.which(args.compiler)
    if compiler is None:
        parser.error('Tectonic was not found. Install it or pass --compiler with its executable path.')
    for number in ([args.tutorial] if args.tutorial else FOLDERS):
        tutorial = ROOT / FOLDERS[number]
        source = tutorial / f'Tutorial_{number}_Exercise_Solutions.tex'
        target = source.with_suffix('.pdf')
        source_hash = sha256(source)
        assets = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', source.read_text(encoding='utf-8'))
        asset_hashes = {}
        for asset in assets:
            asset_path = (tutorial / asset).resolve()
            if not asset_path.is_relative_to(tutorial / 'assets') or not asset_path.is_file():
                raise ValueError(f'Missing or unstable document asset: {asset}')
            asset_hashes[asset] = sha256(asset_path)
        # All compiler intermediates stay outside the repository.
        with tempfile.TemporaryDirectory(prefix=f'tutorial-{number}-solutions-') as scratch:
            subprocess.run([compiler, '--untrusted', '--outdir', scratch, source.name], cwd=tutorial, check=True)
            built = Path(scratch) / target.name
            reader = PdfReader(built)
            if reader.is_encrypted or not reader.pages:
                raise ValueError(f'Invalid compiled PDF: {target.name}')
            pages = len(reader.pages)
            del reader
            if sha256(source) != source_hash or any(sha256(tutorial / asset) != value for asset, value in asset_hashes.items()):
                raise ValueError('Source or assets changed during compilation; no PDF was published.')
            shutil.copyfile(built, target)
        record = {
            'source': source.name, 'source_sha256': source_hash,
            'pdf': target.name, 'pdf_sha256': sha256(target), 'assets': asset_hashes,
            'command': f'python scripts/build_solutions.py --tutorial {number}',
        }
        record_path = tutorial / 'assets/solutions_build.json'
        record_path.parent.mkdir(exist_ok=True)
        record_path.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
        print(f'Built {target.name}: {pages} pages; source/PDF integrity record updated.')


if __name__ == '__main__':
    main()
