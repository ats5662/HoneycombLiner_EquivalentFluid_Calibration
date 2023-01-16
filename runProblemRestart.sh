#!/bin/sh
7z x HexLinerMeshMeterTet4.7z 
dakota -i dakotaInputDeck.in -o output.log -read_restart dakota.rst