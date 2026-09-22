# Tutorial 1 — LV Voltage Estimation with Keras

Train a neural network to estimate 31 customer voltages from 62 active/reactive power inputs. You will prepare simulated data, compare model settings with blocked K-fold validation, compare random seeds, train a final model and assess it on a separate test period.

This tutorial is intended for electrical engineering students in the Power specialisation. No previous neural-network experience is required.

## Open in Google Colab

<a target="_blank" href="https://colab.research.google.com/github/Team-Nando/Capstone_project_2026_DEMO/blob/main/Tutorial_1_LV_Voltage_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open Tutorial 1 in Colab"></a>

1. Click the badge and read the notebook introduction.
2. Choose **Runtime > Run all**. The first code cell clones the repository and installs the required packages.
3. If Colab asks for a runtime restart, restart and choose **Runtime > Run all** again.
4. Allow the model-selection cells to finish. A progress line is printed after each candidate or seed has been evaluated.
5. Download the generated CSV files from `Tutorial_1_LV_Voltage_Estimation/results/` in Colab's Files panel before the runtime ends.

No Google Drive mount, notebook upload or data upload is needed. A new runtime clones a fresh copy of the repository. Only load the included pickle files from a trusted source.

## Run locally

From the repository root, run:

```shell
python -m pip install -r requirements.txt
jupyter lab
```

Alternatively, from this Tutorial 1 folder, run:

```shell
python -m pip install -r requirements.txt
jupyter lab
```

Open `Tutorial_1_LV_Voltage_Estimation.ipynb` and run its cells in order. If Jupyter is started elsewhere, set `tutorial_path` in Section 2.2.2 to this folder.

## Files

| Item | Path |
|---|---|
| Student notebook | `Tutorial_1_LV_Voltage_Estimation.ipynb` |
| Local dependencies | `requirements.txt` |
| Simulated training/test data | `synthentic_data_5_min_LV/` |
| Circuit image | `LVnetwork-topology.png` |
| Generated and verified result tables | `results/` |

The existing `synthentic` spelling in the supplied data-folder name is retained to avoid breaking the data paths.

## Early stopping and model selection

The earlier quick/full choice only changed the epoch candidates, so it has been removed. The notebook now uses one reproducible workflow:

- Eight hyperparameter combinations are evaluated with three blocked folds (**24 fits**).
- Each validation fit may run for at most **300 epochs**.
- Training stops after **20 epochs** without a validation-loss improvement of at least `1e-5`.
- `restore_best_weights=True` restores the weights from the best validation epoch.
- Ten seeds are compared using the selected settings (**30 fits**).
- The final epoch count is the median best epoch from the selected seed's three folds.
- A fresh final model is trained for that fixed count on **all training rows** (**1 fit**).

This gives 55 fits in the standard workflow. The safety limit prevents an unbounded run; it is not a second training mode. Test data are never used for early stopping, hyperparameter selection or seed selection.

The result tables are saved as:

- `results/LV_keras_search_results.csv`
- `results/LV_keras_seed_results.csv`
- `results/LV_keras_test_metrics.csv`

Rerunning the workflow replaces these generated tables. Numerical results may vary slightly across environments.

## Exercises

Two exercise groups contain seven practical coding tasks: E1.1–E1.3 and E2.1–E2.4. Run Sections 2.2–2.4 before using the Exercise Workspace. The exercises reuse the early-stopping functions but keep their models and variables separate from the main tutorial workflow.
