# Neural Network-Based LV Voltage Estimation Tutorial

This repository contains Part 1 of an AI-based voltage-estimation tutorial for
low-voltage distribution networks. The notebook covers data inspection,
leakage-safe normalisation, neural-network training, blocked K-fold
hyperparameter selection, multi-seed selection and held-out test evaluation.

## Files

- `Tutorial_1_LV_Voltage_Estimation.ipynb`: complete tutorial notebook.
- `LVnetwork-topology.png`: LV test-network diagram used by the notebook.
- `LV_search_results.csv`: completed blocked K-fold search results.
- `LV_final_seed_results.csv`: completed random-seed comparison results.
- `requirements.txt`: Python dependencies for local execution.

## Dataset

The dataset is not included until its redistribution permission is confirmed.
Place the approved data package beside the notebook using this structure:

```text
synthentic_data_5_min_LV/
├── training/
│   ├── PQ.pkl
│   └── V.pkl
└── test/
    ├── PQ.pkl
    └── V.pkl
```

The source folder intentionally retains the original `synthentic` spelling.

## Run locally

```powershell
python -m pip install -r requirements.txt
jupyter lab
```

Open `Tutorial_1_LV_Voltage_Estimation.ipynb` and run the cells in order.

## Google Colab

After this folder has been uploaded to GitHub, the existing notebook can be
opened directly in Google Colab. No separate Colab notebook is required. The
approved dataset must still be made available in the Colab session before the
data-loading section is run.
