# AI-Based Voltage Estimation Tutorials

Two Keras tutorials for electrical engineering students in the **Power specialization**. No previous neural-network experience is required; start with Tutorial 1.

All P, Q and voltage values are **simulated data**, not real customer measurements. The models estimate customer voltages from inputs at the same time step; they do not forecast future voltages.

## Choose a tutorial

| Tutorial | Notebook | Instructions | Colab data package |
|---|---|---|---|
| 1. Estimate LV voltages from P/Q | [Notebook](Tutorial_1_LV_Vol_Estimation/Tutorial_1_LV_Voltage_Estimation_Keras_v2_0.ipynb) | [Guide](Tutorial_1_LV_Vol_Estimation/README_Keras_v2_0.md) | [ZIP](Tutorial_1_LV_Vol_Estimation/Tutorial_1_Keras_v2_0_colab_data.zip) |
| 2. Add reference voltages to account for upstream MV effects | [Notebook](Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_MV_Effects_Reference_Voltage_Keras_v2_0.ipynb) | [Guide](Tutorial_2_MV_Effects_Reference_Voltage/README_Keras_v2_0.md) | [ZIP](Tutorial_2_MV_Effects_Reference_Voltage/Tutorial_2_Keras_v2_0_colab_data.zip) |

## Run locally

Keep the two tutorial folders next to each other. Tutorial 2 reads the LV data from Tutorial 1 and the MV-scenario data from its own folder:

```text
Capstone_project_2026_sem1-main/
  Tutorial_1_LV_Vol_Estimation/
    synthentic_data_5_min_LV/
      training/  (PQ.pkl, V.pkl)
      test/      (PQ.pkl, V.pkl)
  Tutorial_2_MV_Effects_Reference_Voltage/
    synthetic_data_5_min_MV/
      training/  (PQ.pkl, V.pkl)
      test/      (PQ.pkl, V.pkl)
```

The existing `synthentic` spelling in Tutorial 1 is intentional. Do not rename it or move the data into a new `data` folder.

From the project folder, install the shared dependencies and start Jupyter:

```shell
python -m pip install -r requirements.txt
jupyter lab
```

Open the chosen notebook and run Sections 2.2-2.6 in order. Keep `RUN_MODE = "quick"` for your first run. You do not need to unpack either Colab ZIP locally or run Tutorial 1 before running Tutorial 2.

If your data are stored elsewhere, edit the individual `DATA_FILES` paths in Section 2.3.1. Keep training and test files separate.

## Run in Google Colab

1. Download the chosen notebook and its matching ZIP from the table above.
2. Open [Google Colab](https://colab.research.google.com/) and choose **File > Upload notebook** to open the `.ipynb` file.
3. Run Section **2.2.1** from the first cell, **Prepare the runtime**. If Colab requests a restart, restart and run from that cell again.
4. When the file-preparation cell shows an upload button, select the matching ZIP. Do not rename or unpack it yourself.
5. Continue with Sections 2.2.2-2.6 in order, using `RUN_MODE = "quick"`.

Each ZIP contains everything its notebook needs. **Tutorial 2's ZIP includes both LV and MV datasets**, so Colab does not need a separate Tutorial 1 upload. No whole-project upload or Google Drive mount is required.

Save the notebook and download the files in `results/quick/` from Colab's Files panel before the runtime ends. Saving the notebook does not save those runtime files. A new runtime requires another ZIP upload. Only use the supplied ZIP and pickle files from a trusted source.

## Exercises and results

Each notebook contains two exercise groups with seven practical coding tasks.

Saved outputs were checked in local quick-mode runs. Live Colab training and full-mode runs have not been verified for this version. Numerical results can vary slightly between environments; see each tutorial guide for details.
