#!/bin/sh

parameters_file=$1
results=$2

dprepro $parameters_file materialInputDeck.template Materials.xml
dprepro $parameters_file harmonicAcousticSimInputDeck.template HexLiner_NIT_HarmonicAcousticSimulation.xml

cfs -d HexLiner_NIT_HarmonicAcousticSimulation > HexLiner_NIT_HarmonicAcousticSimulation.log

rm *.cdb
rm -rf results_hdf5
cp history/* .
rm -rf history

python3 calcSimResults.py

rm Hex_PLA_1_AllData.csv
rm Hex_PLA_2_AllData.csv
rm Hex_PLA_3_AllData.csv
rm Hex_TPU_1_AllData.csv
rm Hex_TPU_2_AllData.csv
rm Hex_TPU_3_AllData.csv

residuals=$(head -n 60 residuals.txt | awk '{print $1}')
echo "$residuals" > $results
