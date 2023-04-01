#!/bin/sh
cp ../HexLinerMeshMeterTet4.7z .
7z x HexLinerMeshMeterTet4.7z
cp ../calcAbsorptionCoefficient.py .
cfs -t4 -d finalMaterialTestInputDeck
cp history/* .
rm -rf history
cp ../Hex_PLA_1_AllData.csv .
cp ../Hex_PLA_2_AllData.csv .
cp ../Hex_PLA_3_AllData.csv .
cp ../Hex_TPU_1_AllData.csv .
cp ../Hex_TPU_2_AllData.csv .
cp ../Hex_TPU_3_AllData.csv .
python plotFinalMaterialTest.py
rm HexLinerMeshMeterTet4.cdb
rm calcAbsorptionCoefficient.py
rm Hex_PLA_1_AllData.csv
rm Hex_PLA_2_AllData.csv
rm Hex_PLA_3_AllData.csv
rm Hex_TPU_1_AllData.csv
rm Hex_TPU_2_AllData.csv
rm Hex_TPU_3_AllData.csv