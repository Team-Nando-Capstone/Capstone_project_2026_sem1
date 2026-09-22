# AI-Based Voltage Estimation Tutorials

Two Keras tutorials for electrical engineering students in the Power specialization. Start with Tutorial 1. All supplied power and voltage data are simulated. The models estimate customer voltages at the same time step; they do not forecast future voltages.

## Tutorials

| Tutorial | Student notebook | Colab data ZIP | Local dependencies | Exercise solutions (LaTeX) | Exercise solutions (PDF) |
|---|---|---|---|---|---|
| 1. LV Voltage Estimation | [Notebook](Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb) | [ZIP](Tutorial_1_LV_Vol_Estimation/Tutorial_1_Colab_Data.zip) | [Requirements](Tutorial_1_LV_Vol_Estimation/requirements_keras.txt) | [LaTeX](Tutorial_1_LV_Vol_Estimation/Tutorial_1_Exercise_Solutions.tex) | [PDF](Tutorial_1_LV_Vol_Estimation/Tutorial_1_Exercise_Solutions.pdf) |
| 2. MV Effects and Reference Voltage | [Notebook](Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_MV_Effects_Reference_Voltage.ipynb) | [ZIP](Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_Colab_Data.zip) | [Requirements](Tutorial_2_MV_Effects_Reference_Voltage/requirements_keras.txt) | [LaTeX](Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_Exercise_Solutions.tex) | [PDF](Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_Exercise_Solutions.pdf) |

See the [Tutorial 1 guide](Tutorial_1_LV_Vol_Estimation/README.md) and [Tutorial 2 guide](Tutorial_2_MV_Effects_Reference_Voltage/README.md) for data paths, training budgets and exercise instructions.

## Run locally

Install dependencies into the Python environment selected by the notebook kernel. From the project root:

```shell
python -m pip install -r requirements.txt
python -m jupyterlab
```

Run Sections 2.2-2.6 in order with `RUN_MODE = "quick"`. Both notebooks support starting from the project root or their own tutorial folder. From another working directory, set `TUTORIAL_DIRECTORY` in Section 2.2.2 to a relative or absolute tutorial path. Relative `DATA_FILES` entries are resolved from that directory once; absolute entries are used directly.

## Run in Colab

[![Tutorial 1 Colab launch badge: Open in Colab](Tutorial2)](https://colab.research.google.com/drive/1HtoyBFzUATTBMBOEqwazzHkHN03kKRhL?usp=sharing)

[![Tutorial 2 Colab launch badge: Open in Colab](Tutorial2)](https://colab.research.google.com/drive/1FBophjTJ5SIb_lFAx1a6_SkUJT9fc__H?usp=sharing)

Upload the chosen notebook, run its runtime-preparation cell, and upload the matching Colab data ZIP when prompted. A whole-project upload is not needed. Download generated results before ending the runtime; saving a notebook does not preserve separate runtime files. Only load trusted ZIP and pickle files.

## Exercise solutions

Each tutorial contains two exercise groups with seven coding tasks. The student TODO cells remain empty. In a fresh kernel, run Sections 2.2-2.4, then use the seven listings in the matching Exercise Solutions document. The main tutorial search does not need to be repeated first.

The LaTeX files are the sources of the PDFs. Install Tectonic, then run `python scripts/build_solutions.py` from the project root. The [build script](scripts/build_solutions.py) rebuilds both PDFs and updates their source/asset checksums together. If the compiler is not on PATH, pass `--compiler path/to/tectonic`. Keep each tutorial's `assets/` directory in place.

Main tutorial results are in `results/tutorial/quick/`; exercise results are in `results/exercises/`, relative to each tutorial folder. These are different experiments and should not be mixed. The small CSV/JSON result files are included alongside the saved notebook outputs. Generated plot files are ignored; the published Tutorial 1 illustration is in its stable `assets/` directory.

## Validation

From the project root:

```shell
python scripts/validate_tutorials.py
```

The validator checks notebook format and syntax, execution state, local links and exact filename case, both Colab data packages, solution sources and PDFs, saved result integrity and matching exercise tables. It does not train models or download data. A PDF build record in each tutorial's `assets/` directory ties the PDF to its LaTeX source.

## Data conventions

- Tutorial 1 uses its own `synthentic_data_5_min_LV` dataset: 62 P/Q inputs and 31 voltage outputs.
- Tutorial 2 uses only `synthentic_data_5_min_mv_secondary`: 62 P/Q inputs, optionally adding three supplied references, and the same 31 voltage outputs. It does not require running Tutorial 1 or loading Tutorial 1 data.
- Preserve the supplied `synthentic` folder spelling. Fit scalers on training data only, choose settings using training folds, and keep test data for evaluation.
- The exact physical extraction node and generation procedure of Tutorial 2's secondary-reference signals are not documented in the supplied package. Do not assume a verified mapping between those three signals and particular customer targets.
