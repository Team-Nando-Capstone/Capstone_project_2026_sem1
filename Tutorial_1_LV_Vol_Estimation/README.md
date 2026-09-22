# Tutorial 1: LV Voltage Estimation

## Overview

Train a Keras neural network to estimate 31 customer voltages from 62 P/Q inputs. Prepare the data, compare settings with blocked K-fold validation, compare random seeds, and evaluate the selected model on a separate test period. All quantities are simulated. This is same-time estimation, not forecasting.

## Files

- [Student notebook](Tutorial_1_LV_Voltage_Estimation.ipynb)
- [Colab data ZIP](Tutorial_1_Colab_Data.zip)
- [Local dependencies](requirements_keras.txt)
- [Exercise solutions (LaTeX)](Tutorial_1_Exercise_Solutions.tex)
- [Exercise solutions (PDF)](Tutorial_1_Exercise_Solutions.pdf)

## Run locally

From this tutorial folder, install dependencies into the notebook kernel's environment and open Jupyter:

```shell
python -m pip install -r requirements_keras.txt
python -m jupyterlab
```

Run Sections 2.2-2.6 in order. Start with `RUN_MODE = "quick"`. The working directory may be this tutorial folder or the project root.

## Run in Colab

1. Upload `Tutorial_1_LV_Voltage_Estimation.ipynb` to Google Colab.
2. Run **Prepare the runtime** in Section 2.2.1; restart if requested, then run from that cell again.
3. Upload `Tutorial_1_Colab_Data.zip` when prompted. Do not rename it.
4. Continue through Sections 2.2-2.6 in order using quick mode.

The ZIP contains this tutorial's four simulated-data files and circuit image. No Google Drive mount is required. Download `Tutorial_1/results/tutorial/quick/` (or `full/`) and any `Tutorial_1/results/exercises/` files before the runtime ends. Saving the notebook does not save these files. Only load trusted ZIP and pickle files.

## Data and paths

Locally, the notebook loads `PQ.pkl` and `V.pkl` from the `training/` and `test/` folders inside `synthentic_data_5_min_LV`. In Colab, the matching folders are under `data/`. Preserve the supplied folder spelling. The input columns are P/Q for 31 customers; the targets are their 31 voltages.

From a different working directory, replace the first assignment in Section 2.2.2 with `TUTORIAL_DIRECTORY = Path("relative/path/to/tutorial")` or an absolute path. The directory is resolved once. In Section 2.3.1, each `DATA_FILES` entry may be relative to that directory or absolute. Do not repeat the tutorial prefix in a relative entry. Missing directories or files raise a clear `FileNotFoundError` before data loading.

## Training and results

- **Quick:** 20/40-epoch candidates, 16 configurations and three folds; ten seeds are compared. Including one final fit, this is 79 training fits.
- **Full:** the same workflow with 1,000/2,000-epoch candidates. This longer workflow has not been rerun for this delivery.
- **Exercises:** 93/155 hidden neurons, tanh/ReLU, fixed 40 epochs and seeds 0/1/2. Both exercise groups together require 22 fits.

Main results are saved to `results/tutorial/<mode>/`; exercise results use `results/exercises/`. Rerunning a workflow replaces its own result files. The saved notebook outputs come from a clean quick run. CSV/JSON files contain its settings, validation scores, test metrics and all 31 customer errors. Exercise tables describe the separate exercise workflow. Small numerical differences can occur between environments.

## Exercises

Complete E1.1-E1.3 followed by E2.1-E2.4. Student TODO cells are intentionally unexecuted and contain no outputs. For the independent solutions, run Sections 2.2-2.4 in a fresh kernel and paste the seven Python listings into the corresponding workspace cells. Sections 2.5-2.6 do not need to be rerun first.

Use training folds to choose settings and seeds; use test data only after those choices are fixed. The exercises reuse the tutorial test period for a classroom comparison, not a new independent evaluation. Do not retune from the test results.

## Build the solutions

From this tutorial folder:

```shell
python ../scripts/build_solutions.py --tutorial 1
```

Install Tectonic first, or pass `--compiler path/to/tectonic`. The script builds the PDF and updates `assets/solutions_build.json` together. The source also works with a standard LaTeX installation using its declared packages; use the build script for the checked-in PDF and its integrity record. The PDF includes the complete solutions, code and recorded exercise results. Keep `assets/exercise_voltage_profiles.png` in place; the published plot does not depend on a generated results directory.
