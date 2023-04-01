import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.interpolate
from calcAbsorptionCoefficient import cac
import os

path = os.getcwd()
file1 = np.array([a for a in os.listdir(path) if a.endswith('mic1.hist')])
file2 = np.array([b for b in os.listdir(path) if b.endswith('mic2.hist')])
mic1 = file1[0]
mic2 = file2[0]
dfSim = cac(mic1, mic2, 150)
dfSim.to_csv("alphaVsFrequency_FINAL.csv", index=False)
plt.rcParams["figure.figsize"] = (20,8)
fig = plt.figure()
ax = plt.axes()
plt.xlim([377, 3400])
plt.ylim([0, 1])
plt.ylabel("Absorption Coefficient")
plt.xlabel("Frequrency (Hz)")
ax.plot(dfSim["f"], dfSim["alpha"]);
plt.savefig('SimResults.png')
dfTest1_PLA = pd.read_csv("Hex_PLA_1_AllData.csv")
dfTest2_PLA = pd.read_csv("Hex_PLA_2_AllData.csv")
dfTest3_PLA = pd.read_csv("Hex_PLA_3_AllData.csv")
dfTest1_TPU = pd.read_csv("Hex_TPU_1_AllData.csv")
dfTest2_TPU = pd.read_csv("Hex_TPU_2_AllData.csv")
dfTest3_TPU = pd.read_csv("Hex_TPU_3_AllData.csv")
dfTestConcatPLA = pd.concat((dfTest1_PLA, dfTest2_PLA, dfTest3_PLA))
dfTestConcatTPU = pd.concat((dfTest1_TPU, dfTest2_TPU, dfTest3_TPU))
dfTestConcatPLA.at[0,"Frequency_Hz"] = 377
dfTestConcatTPU.at[0,"Frequency_Hz"] = 377
by_row_index_pla = dfTestConcatPLA.groupby(dfTestConcatPLA.index)
dfMeansPLA = by_row_index_pla.mean().rename(columns={"Absorption_Coefficient": "Absorption_Coefficient_PLA"})
dfMeansPLA = dfMeansPLA[["Frequency_Hz", "Absorption_Coefficient_PLA"]]
by_row_index_tpu = dfTestConcatTPU.groupby(dfTestConcatTPU.index)
dfMeansTPU = by_row_index_tpu.mean().rename(columns={"Absorption_Coefficient": "Absorption_Coefficient_TPU"})
dfMeansTPU = dfMeansTPU[["Frequency_Hz", "Absorption_Coefficient_TPU"]]
pd.concat([dfMeansPLA.set_index('Frequency_Hz'),dfMeansTPU.set_index('Frequency_Hz')], axis=1, join='inner').to_csv("alphaVsFrequency_AvgNIT.csv", index=False)
frequencyArray = np.linspace(377, 3400, 150)
alphaSimInterpFunc = scipy.interpolate.Akima1DInterpolator(dfSim["f"], dfSim["alpha"])
alphaSimValue = alphaSimInterpFunc(frequencyArray)
alphaTestInterpFunc = scipy.interpolate.Akima1DInterpolator(dfMeansPLA["Frequency_Hz"], dfMeansPLA["Absorption_Coefficient_PLA"])
alphaTestValue = alphaTestInterpFunc(frequencyArray)
alpha_residuals = alphaSimValue - alphaTestValue
np.savetxt("residuals.txt", alpha_residuals, delimiter=" ", fmt="%f")
SSE = np.sum(alpha_residuals**2)
with open('SSE.txt', 'w') as f:
  f.write('%f' % SSE)
  f.close()
MAE = np.mean(np.abs(alpha_residuals))
with open('MAE.txt', 'w') as f:
  f.write('%f' % MAE)
  f.close()
RMSE = np.sqrt(np.mean(alpha_residuals**2))
with open('RMSE.txt', 'w') as f:
  f.write('%f' % RMSE)
  f.close()
