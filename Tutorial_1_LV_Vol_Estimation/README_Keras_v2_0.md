# Tutorial 1 - LV Voltage Estimation with Keras

For electrical engineering students in the **Power specialization**, with no previous neural-network experience. All P, Q and voltage values are **simulated**, not real customer measurements.

## What you will do

Train a neural network to estimate 31 customer voltages from 62 P/Q inputs. You will prepare the data, compare model settings with blocked K-fold validation, compare random seeds, and check the chosen model on a separate test period.

## Files to use

- [Student notebook](Tutorial_1_LV_Voltage_Estimation_Keras_v2_0.ipynb)
- [Colab data ZIP](Tutorial_1_Keras_v2_0_colab_data.zip)
- [Local dependencies](requirements_keras.txt)
- [English exercise answers (PDF)](Tutorial_1_Keras_v2_0_Exercise_Solutions_EN.pdf)
- [Saved quick-mode results](results/quick/)

## Run locally

1. Open a terminal in this Tutorial 1 folder and run:

   ```shell
   python -m pip install -r requirements_keras.txt
   jupyter lab
   ```

2. Open the student notebook and run Sections **2.2-2.6** in order.
3. Keep `RUN_MODE = "quick"` for your first run.

The notebook reads `PQ.pkl` and `V.pkl` from the `training` and `test` subfolders of `synthentic_data_5_min_LV`. Keep the existing `synthentic` spelling. The Colab ZIP is not needed locally.

The working directory may be this tutorial folder or the project root. If you start elsewhere, set `TUTORIAL_DIRECTORY = Path("your/tutorial/folder")` in Section 2.2.2. If the data are elsewhere, edit the four `DATA_FILES` paths in Section 2.3.1 individually; they do not have to share one folder.

## Run in Google Colab

1. Open [Google Colab](https://colab.research.google.com/), choose **File > Upload notebook**, and select `Tutorial_1_LV_Voltage_Estimation_Keras_v2_0.ipynb`.
2. Run Section **2.2.1** from the first cell, **Prepare the runtime**. Wait for the library installation to finish. If Colab requests a restart, restart and run from that cell again.
3. When the file-preparation cell shows an upload button, select **`Tutorial_1_Keras_v2_0_colab_data.zip`**. Do not rename or unpack it yourself.
4. Continue with Sections **2.2.2-2.6** in order, using `RUN_MODE = "quick"`.

Only the notebook and its ZIP are needed. The ZIP contains all four simulated-data files and the circuit image. No Google Drive mount is required. Figure 1 is already embedded in the notebook.

Save the notebook and download the files in `results/quick/` from Colab's Files panel before the runtime ends. Saving the notebook does not save those runtime files. A new runtime requires another ZIP upload. Only use the supplied ZIP and pickle files from a trusted source.

## Training and results

- **Quick:** compare 20 and 40 epochs during model selection.
- **Full:** compare 1,000 and 2,000 epochs; this takes much longer.

Both modes include blocked K-fold validation and seed comparison. Results are recalculated and saved under `results/quick/` or `results/full/`. Rerunning a mode replaces its result files, but does not change the simulated data.

The supplied outputs come from a verified local quick-mode run. Live Colab training and full-mode runs have not been verified for this version. Numerical results can vary slightly between environments.

## Exercises

Two exercise groups contain seven practical coding tasks: E1.1-E1.3 and E2.1-E2.4. No written explanation questions are required.

Run Sections **2.2-2.4** before using the Exercise Workspace or the PDF answer code. The exercises use a fixed **40-epoch** budget, independent of `RUN_MODE`. Keep exercise models and results separate from the main tutorial results.
