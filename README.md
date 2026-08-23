# AI-Based Voltage Estimation Tutorials

This repository contains an AI-based voltage-estimation tutorial sequence for
low-voltage distribution networks.

- **Part 1** introduces neural-network-based LV voltage estimation from P/Q
  smart-meter inputs.
- **Part 2** studies MV upstream effects and shows how reference voltage
  measurements can recover the missing information.

All P, Q and voltage values used in these tutorials are **simulated data**. The
files do not contain real customer or real distribution-network measurements.

## Files

### Part 1: LV Voltage Estimation

- `Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb`:
  Part 1 tutorial notebook.
- `Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation_Exercise_Solutions.ipynb`:
  Part 1 exercise solutions for E.1-E.3.
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

### Part 2: MV Effects and Reference Voltage

- `Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_MV_Effects_Reference_Voltage.ipynb`:
  Part 2 tutorial notebook.
- `Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_MV_Effects_Reference_Voltage_Exercise_Solutions.ipynb`:
  Part 2 exercise solutions for E.1-E.3.
- `Tutorial_2_MV_Effects_Reference_Voltage/data/`: simulated fixed-upstream
  LV and varying-upstream MV datasets.
- `Tutorial_2_MV_Effects_Reference_Voltage/network/`: MG1 topology diagram and
  customer topology table.
- `Tutorial_2_MV_Effects_Reference_Voltage/results/`: saved result tables used
  by the tutorial.
- `Tutorial_2_MV_Effects_Reference_Voltage/requirements.txt`: dependencies for
  running the tutorial folder directly.

## Simulated Datasets

The simulated data are included with the tutorials. In Part 1, they are stored
as four separate files under the `training` and `test` subfolders:

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

Part 2 uses two datasets:

```text
Tutorial_2_MV_Effects_Reference_Voltage/
  data/
    synthetic_data_5_min_LV/
      training/
        PQ.pkl
        V.pkl
      test/
        PQ.pkl
        V.pkl
    synthetic_data_5_min_MV/
      training/
        PQ.pkl
        V.pkl
      test/
        PQ.pkl
        V.pkl
```

The supplied training and test periods must remain separate so that the final
test data are not used during normalisation, model tuning or model selection.

## Run Locally

```powershell
python -m pip install -r requirements.txt
jupyter lab
```

Open a tutorial notebook from its tutorial folder and run the cells in order.

## Google Colab

[Open tutorial in Colab](https://colab.research.google.com/github/Team-Nando-Capstone/Capstone_project_2026_sem1/blob/main/Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb)

[Open exercise solutions in Colab](https://colab.research.google.com/github/Team-Nando-Capstone/Capstone_project_2026_sem1/blob/main/Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation_Exercise_Solutions.ipynb)

Part 2 Colab links will be added after the Colab folder layout is finalised.
