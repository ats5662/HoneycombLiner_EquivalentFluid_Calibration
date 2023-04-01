import numpy as np
import pandas as pd
import scipy.interpolate
from calcAbsorptionCoefficient import cac
import os

path = os.getcwd()
file1 = np.array([a for a in os.listdir(path) if a.endswith('mic1.hist')])
file2 = np.array([b for b in os.listdir(path) if b.endswith('mic2.hist')])
mic1 = file1[0]
mic2 = file2[0]
fSamples = 60
dfSim = cac(mic1, mic2, fSamples)
dfSim.to_csv("alphaVsFrequency.csv", index=False)

dfTest1_PLA = pd.read_csv("Hex_PLA_1_AllData.csv")
dfTest2_PLA = pd.read_csv("Hex_PLA_2_AllData.csv")
dfTest3_PLA = pd.read_csv("Hex_PLA_3_AllData.csv")
dfTest1_TPU = pd.read_csv("Hex_TPU_1_AllData.csv")
dfTest2_TPU = pd.read_csv("Hex_TPU_2_AllData.csv")
dfTest3_TPU = pd.read_csv("Hex_TPU_3_AllData.csv")

dfTestConcat = pd.concat((dfTest1_PLA, dfTest2_PLA, dfTest1_PLA))
dfTestConcat.at[0,"Frequency_Hz"] = 377
by_row_index = dfTestConcat.groupby(dfTestConcat.index)
dfTestMeans = by_row_index.mean()

frequencyArray = np.linspace(377, 3400, fSamples)

#simulation
alphaSimInterpFunc = scipy.interpolate.Akima1DInterpolator(dfSim["f"], dfSim["alpha"])
alphaSimValue = alphaSimInterpFunc(frequencyArray)

#test nit
alphaTestInterpFunc = scipy.interpolate.Akima1DInterpolator(dfTestMeans["Frequency_Hz"], dfTestMeans["Absorption_Coefficient"])
alphaTestValue = alphaTestInterpFunc(frequencyArray)

alpha_residuals = alphaSimValue - alphaTestValue
np.savetxt("residuals.txt", alpha_residuals, delimiter=" ", fmt="%f")
