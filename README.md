# HoneycombLiner_EquivalentFluid_Calibration

Clone and compile openCFS, directions at the link below

https://gitlab.com/openCFS/cfs

Alternatively download the binary packages at the link below

https://gitlab.com/openCFS/cfs/-/releases

---

Download DAKOTA binary or source code and compile at the link below 

https://dakota.sandia.gov/sites/default/files/docs/6.17.0-release/user-html/setupdakota.html

---

Python environment

```
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/venv/bin/activate
```

Clone this repository and navigate to folder

```
git clone https://github.com/ats5662/HexLiner_Facesheet_Calibration.git
cd HexLiner_Facesheet_Calibration
```
or 

```
git clone git@github.com:ats5662/HexLiner_Facesheet_Calibration.git
cd HexLiner_Facesheet_Calibration
```
install python packages

```
pip install -r requirements.txt
```

Run problem 

```
./runProblem.sh
```

Run problem with restart file

```
./runProblemRestart.sh
```

