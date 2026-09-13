# Tutorial 2 - MV Effects and Reference Voltage with Keras

For electrical engineering students in the **Power specialization** who have worked through Tutorial 1. All P, Q and voltage values are **simulated**, not real customer measurements.

## What you will do

Compare two neural networks: one uses 62 P/Q inputs; the other adds three reference voltages at customers C1-C3. Both estimate the same 28 customer voltages, C4-C31.

Both models are trained on the varying-upstream dataset. The fixed-upstream dataset is used only to examine the upstream effect. Reference voltages are assumed available when making predictions; target customer voltages are not used as inputs.

You will use blocked K-fold validation and seed comparison to choose shared settings, then compare the two models on a separate test period.

## Files to use

- [Student notebook](Tutorial_2_MV_Effects_Reference_Voltage_Keras_v2_0.ipynb)
- [Colab data ZIP](Tutorial_2_Keras_v2_0_colab_data.zip)
- [Local dependencies](requirements_keras.txt)
- [Saved quick-mode results](results/quick/)

## Run locally

1. Keep the Tutorial 1 and Tutorial 2 folders next to each other under the project folder.
2. Open a terminal in this Tutorial 2 folder and run:

   ```shell
   python -m pip install -r requirements_keras.txt
   jupyter lab
   ```

3. Open the student notebook and run Sections **2.2-2.6** in order.
4. Keep `RUN_MODE = "quick"` for your first run.

The default data locations are:

- **LV data:** `synthentic_data_5_min_LV` inside the neighbouring `Tutorial_1_LV_Vol_Estimation` folder.
- **MV-scenario data:** `synthetic_data_5_min_MV` inside this Tutorial 2 folder.

Each dataset has `training` and `test` subfolders containing `PQ.pkl` and `V.pkl`. No local `data` folder or Colab ZIP extraction is needed. Tutorial 1's data must be present, but you do not need to run its notebook first.

The working directory may be this tutorial folder or the project root. If you start elsewhere, set `TUTORIAL_DIRECTORY = Path("your/tutorial/folder")` in Section 2.2.2. If the data are elsewhere, edit the eight `DATA_FILES` paths in Section 2.3.1 individually; they do not have to share one folder.

## Run in Google Colab

1. Open [Google Colab](https://colab.research.google.com/), choose **File > Upload notebook**, and select `Tutorial_2_MV_Effects_Reference_Voltage_Keras_v2_0.ipynb`.
2. Run Section **2.2.1** from the first cell, **Prepare the runtime**. Wait for the library installation to finish. If Colab requests a restart, restart and run from that cell again.
3. When the file-preparation cell shows an upload button, select **`Tutorial_2_Keras_v2_0_colab_data.zip`**. Do not rename or unpack it yourself.
4. Continue with Sections **2.2.2-2.6** in order, using `RUN_MODE = "quick"`.

Only the notebook and its ZIP are needed. **This ZIP contains both LV and MV datasets**, plus the network files. No separate Tutorial 1 upload or Google Drive mount is required. Figure 1 is already embedded in the notebook.

Save the notebook and download the files in `results/quick/` from Colab's Files panel before the runtime ends. Saving the notebook does not save those runtime files. A new runtime requires another ZIP upload. Only use the supplied ZIP and pickle files from a trusted source.

## Training and results

- **Quick:** 40 epochs per model, with 44 model fits across model selection, seed comparison and final training.
- **Full:** the same workflow with 300 epochs per model; this takes much longer.

Results are recalculated and saved under `results/quick/` or `results/full/`. The files include model-setting and seed comparisons, overall and per-customer test errors, and run settings. Rerunning a mode replaces its result files, but does not change the simulated data.

The supplied outputs come from a verified local quick-mode run. Live Colab training and full-mode runs have not been verified for this version. Numerical results can vary slightly between environments.

## Exercises

Two exercise groups contain seven practical coding tasks: E1.1-E1.3 and E2.1-E2.4. No written explanation questions are required.

Run Sections **2.2-2.4** before using the Exercise Workspace. Compare relu models with 93 and 155 hidden neurons, using a fixed **40-epoch** budget, independent of `RUN_MODE`. Keep exercise models and results separate from the main tutorial results. Reusing the test period here is a classroom comparison, not a new independent test.
