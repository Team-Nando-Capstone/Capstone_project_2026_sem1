# Neural Network-Based LV Voltage Estimation Tutorial

This repository contains Part 1 of an AI-based voltage-estimation tutorial for
low-voltage distribution networks. The notebook covers data inspection,
leakage-safe normalisation, neural-network training, blocked K-fold
hyperparameter selection, multi-seed selection and held-out test evaluation.

All P, Q and voltage values used in this tutorial are **simulated data**. The
files do not contain real customer or real distribution-network measurements.

## Files

- `Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb`:
  English tutorial notebook.
- `Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation_Exercise_Solutions.ipynb`:
  exercise solutions for E.1-E.3.
- `Tutorial_1_LV_Vol_Estimation/LVnetwork-topology.png`: LV test-network
  diagram used by the notebook.
- `Tutorial_1_LV_Vol_Estimation/LV_search_results.csv`: completed blocked
  K-fold search results.
- `Tutorial_1_LV_Vol_Estimation/LV_final_seed_results.csv`: completed
  random-seed comparison results.
- `Tutorial_1_LV_Vol_Estimation/synthentic_data_5_min_LV/`: simulated
  training and test data.
- `Tutorial_1_LV_Vol_Estimation/requirements.txt`: dependencies for running
  the tutorial folder directly.
- `requirements.txt`: root-level dependency file for repository setup.

## Simulated Dataset

The simulated data are included with the tutorial. They are stored as four
separate files under the `training` and `test` subfolders:

```text
Tutorial_1_LV_Vol_Estimation/
  synthentic_data_5_min_LV/
    training/
      PQ.pkl
      V.pkl
    test/
      PQ.pkl
      V.pkl
```

The source folder intentionally retains the original `synthentic` spelling.
The supplied training and test periods must remain separate so that the final
test data are not used during normalisation, model tuning or model selection.

## Run Locally

```powershell
python -m pip install -r requirements.txt
jupyter lab
```

Open the tutorial notebook from `Tutorial_1_LV_Vol_Estimation/` and run the
cells in order.

## Google Colab

[Open tutorial in Colab](https://colab.research.google.com/github/Team-Nando-Capstone/Capstone_project_2026_sem1/blob/main/Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb)

[Open exercise solutions in Colab](https://colab.research.google.com/github/Team-Nando-Capstone/Capstone_project_2026_sem1/blob/main/Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation_Exercise_Solutions.ipynb)
