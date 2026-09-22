# AI-Based Voltage Estimation Tutorials

This repository contains **Tutorial 1: LV Voltage Estimation with Keras**. It is written for electrical engineering students in the Power specialisation; no previous neural-network experience is required.

All P, Q and voltage values are **simulated data**, not real customer measurements. The model estimates customer voltages from P/Q values at the same time step; it does not forecast future voltages.

The repository keeps each tutorial in its own numbered folder, so Tutorial 2 can be added later without changing the Tutorial 1 paths.

## Run Tutorial 1 in Google Colab

<a target="_blank" href="https://colab.research.google.com/github/Team-Nando/Capstone_project_2026_DEMO/blob/main/Tutorial_1_LV_Voltage_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open Tutorial 1 in Colab"></a>

1. Click the badge above. Colab opens the notebook directly from GitHub.
2. Read the introduction, then choose **Runtime > Run all**.
3. If Colab asks to restart the runtime after installing packages, restart it and choose **Runtime > Run all** again.
4. Keep the browser tab open while the model search runs. Early stopping ends a training run when its validation loss stops improving.
5. Before the Colab runtime ends, download the CSV files from `Tutorial_1_LV_Voltage_Estimation/results/` in the Files panel. Saving the notebook does not save separate runtime files.

The setup cell clones this public repository into the Colab runtime and installs the required packages. No Google Drive mount, notebook upload or separate data upload is needed. Only load the included pickle files from a trusted copy of this repository.

## Run Tutorial 1 locally

Download the complete repository with GitHub's **Code > Download ZIP** option and extract it, or clone it:

```shell
git clone https://github.com/Team-Nando/Capstone_project_2026_DEMO.git
cd Capstone_project_2026_DEMO
```

Install the dependencies and start Jupyter from the repository root:

```shell
python -m pip install -r requirements.txt
jupyter lab
```

Open [`Tutorial_1_LV_Voltage_Estimation.ipynb`](Tutorial_1_LV_Voltage_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb) and run the cells in order. The notebook also works when Jupyter is started inside the Tutorial 1 folder.

## Tutorial 1 files

| Item | Location |
|---|---|
| Notebook | [`Tutorial_1_LV_Voltage_Estimation.ipynb`](Tutorial_1_LV_Voltage_Estimation/Tutorial_1_LV_Voltage_Estimation.ipynb) |
| Detailed guide | [`Tutorial_1_LV_Voltage_Estimation/README.md`](Tutorial_1_LV_Voltage_Estimation/README.md) |
| Dependencies | [`Tutorial_1_LV_Voltage_Estimation/requirements.txt`](Tutorial_1_LV_Voltage_Estimation/requirements.txt) |
| Simulated data | `Tutorial_1_LV_Voltage_Estimation/synthentic_data_5_min_LV/` |
| Verified result tables | `Tutorial_1_LV_Voltage_Estimation/results/` |

The existing `synthentic` spelling in the supplied data-folder name is retained to avoid breaking the data paths.

## Training workflow

The notebook uses three blocked folds to compare eight hyperparameter combinations, then compares ten random seeds. There are no separate quick and full modes. Every validation fit has a 300-epoch safety limit and uses early stopping with a patience of 20 epochs and a minimum validation-loss improvement of `1e-5`. The best weights are restored automatically.

The final epoch count is the median best epoch from the selected seed's three validation folds. A fresh model is then trained for that fixed number of epochs using all training rows. The separate test period is used only for the final performance check.

Numerical results may vary slightly across hardware and software environments.
