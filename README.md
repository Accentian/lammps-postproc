# Uses Python in Jupyter Notebook or any IDE that supports Python

This repo contains a series of Python scripts designed to process data after a successful LAMMPS run.

  1. "thermal_conductivity_calculations.ipynb (OUTDATED)"
This Python code was created in Jupyter Notebook. It reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of `Step`, `Temp`, and `c_myFlux[1]` are located. It will then parse only the c_myFlux[1] column for thermal conductivity calculations.

  2. "thermal_conductivity_calc.py"
This Python script is identical to `thermal_conductivity_calculations.ipynb`. Ensure that the imports or Python environments for numpy and matplotlib.pyplot exists in order for the script to work. Like the first listing, the script reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of Step, Temp, and c_myFlux[1] are located. It will then parse only the `c_myFlux[1]` column for thermal conductivity calculations.

  3. "v2thermal_conductivity_calc.py"
This Python script is work in-progress script that's similar to `thermal_conductivity_calc.py`. Ensure that the imports or Python environments for numpy and matplotlib.pyplot exists in order for the script to work. Like the first listing, the script reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of Step, Temp, and c_myFlux[1] are located. It will then parse only the `c_myFlux[1]` column for thermal conductivity calculations using user defined functions.

TO RUN THE SCRIPT(S) & RESULTS:
  - Make sure `Thermal_CNT_0_25_1.96.log.lammps` is in the same folder as the Python script. Make any necessary changes in the script regarding file paths, etc., and then run the script.
  - From `Thermal_CNT_0_25_1.96.log.lammps`, a .csv file (`Thermal_CNT_0_25_1.96.csv`) will be created
  - From `Thermal_CNT_0_25_1.96.log.lammps`, a PNG image (`Thermal_CNT_0_25_1.96_HeatFlux.png`) will be created
