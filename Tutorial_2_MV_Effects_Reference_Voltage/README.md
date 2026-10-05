# Tutorial 2: MV Effects and Reference Voltage

## Overview

Train two Keras neural networks under varying upstream conditions: P/Q only, and P/Q plus three supplied reference voltages. Compare their estimates for the same 31 customers. All quantities are simulated. This is same-time estimation, not forecasting. Tutorial 1 provides the background, but no previous model run or Tutorial 1 dataset is required.

## Files

- [Student notebook](Tutorial_2_MV_Effects_Reference_Voltage.ipynb)
- [Colab data ZIP](Tutorial_2_Colab_Data.zip)
- [Local dependencies](requirements_keras.txt)
- [Exercise solutions (LaTeX)](Tutorial_2_Exercise_Solutions.tex)
- [Exercise solutions (PDF)](Tutorial_2_Exercise_Solutions.pdf)

## Run locally

From this tutorial folder, install dependencies into the notebook kernel's environment and open Jupyter:

```shell
python -m pip install -r requirements_keras.txt
python -m jupyterlab
```

Run Sections 2.2-2.6 in order. Start with `RUN_MODE = "quick"`. The working directory may be this tutorial folder or the project root.

## Run in Colab

1. Open the GitHub notebook in Colab: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Team-Nando-Capstone/Capstone_project_2026_sem1/blob/main/Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_MV_Effects_Reference_Voltage.ipynb)
2. Run **Prepare the runtime** in Section 2.2.1; restart if requested, then run from that cell again.
3. Continue through Sections 2.2-2.6 in order using quick mode.

In Colab, the preparation cell clones this GitHub repository into the temporary runtime and reads this tutorial's checked-in data and network files directly, so no notebook or ZIP upload is needed. Everyone can edit and run their own Colab session without changing the GitHub original; opening the badge again starts from the GitHub version. Download `results/tutorial/quick/` (or `full/`) and any `results/exercises/` files before the runtime ends. Saving a notebook does not preserve separate runtime files.

## Data and paths

`synthentic_data_5_min_mv_secondary/training_tx/` and `test_tx/` each contain `PQ.pkl`, `V.pkl` and `V_secondary.pkl`. Preserve the supplied folder spelling. Keep `network/customer_topology.csv` and the network image in `network/`.

The two input sets contain 62 and 65 columns and share all 31 voltage targets. The extra columns are `phase_a`, `phase_b` and `phase_c` from the supplied secondary-reference file, not the first three customer-voltage columns. Their exact physical extraction node and generation procedure are undocumented. Do not assume a verified reference-to-customer mapping. These signals must be available at prediction time.

From a different working directory, replace the first assignment in Section 2.2.2 with `TUTORIAL_DIRECTORY = Path("relative/path/to/tutorial")` or an absolute path. The directory is resolved once. In Section 2.3.1, each `DATA_FILES` entry may be relative to that directory or absolute. Do not repeat the tutorial prefix in a relative entry. Missing directories or files raise a clear `FileNotFoundError` before data loading.

## Training and results

- **Quick:** tanh, 20/40-epoch candidates, eight configurations, three folds and two models; three seeds are compared. Including two final fits, this is 68 training fits.
- **Full:** the same workflow with 1,000/2,000-epoch candidates. This longer workflow has not been rerun for this delivery.
- **Exercises:** ReLU, 93/155 hidden neurons, fixed 40 epochs and seeds 0/1/2. Both exercise groups together require 32 fits.

Main results are saved to `results/tutorial/<mode>/`; exercise results use `results/exercises/`. Rerunning a workflow replaces its own result files. The saved notebook outputs come from a clean quick run. CSV/JSON files contain its settings, validation scores, test metrics and all 31 customer errors. Exercise tables describe the separate exercise workflow. Small numerical differences can occur between environments.

## Exercises

Complete E1.1-E1.3 followed by E2.1-E2.4. Student TODO cells are intentionally unexecuted and contain no outputs. For the independent solutions, run Sections 2.2-2.4 in a fresh kernel and paste the seven Python listings into the corresponding workspace cells. Sections 2.5-2.6 do not need to be rerun first.

Use training folds to choose settings and seeds; use test data only after those choices are fixed. The exercises reuse the tutorial test period for a classroom comparison, not a new independent evaluation. Do not retune from the test results.

## Build the solutions

From this tutorial folder:

```shell
python ../scripts/build_solutions.py --tutorial 2
```

Install Tectonic first, or pass `--compiler path/to/tectonic`. The script builds the PDF and updates `assets/solutions_build.json` together. The source also works with a standard LaTeX installation using its declared packages; use the build script for the checked-in PDF and its integrity record. The PDF includes the complete solutions, code and recorded exercise results. E2.4 generates the comparison plot when its code is run; no external plot file is required to compile this document.
