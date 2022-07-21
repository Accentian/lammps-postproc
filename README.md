# Uses Python in Jupyter Notebook or any IDE that supports Python

This repo contains a series of Python scripts designed to process data after a successful LAMMPS run.

  1. thermal_conductivity_calculations.ipynb (OUTDATED) - 
This Python code was created in Jupyter Notebook. It reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of `Step`, `Temp`, and `c_myFlux[1]` are located. It will then parse only the c_myFlux[1] column for thermal conductivity calculations.

  2. thermal_conductivity_calc.py - 
This Python script is identical to `thermal_conductivity_calculations.ipynb`. Ensure that the imports or Python environments for numpy and matplotlib.pyplot exists in order for the script to work. Like the first listing, the script reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of Step, Temp, and c_myFlux[1] are located. It will then parse only the `c_myFlux[1]` column for thermal conductivity calculations.

  3. v2thermal_conductivity_calc.py - 
This Python script is work in-progress script that's similar to `thermal_conductivity_calc.py`. Ensure that the imports or Python environments for numpy and matplotlib.pyplot exists in order for the script to work. Like the first listing, the script reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of Step, Temp, and c_myFlux[1] are located. It will then parse only the `c_myFlux[1]` column for thermal conductivity calculations using user defined functions.

TO RUN THE SCRIPT(S) & RESULTS:
  - Make sure `Thermal_CNT_0_25_1.96.log.lammps` (or any log.lammps in this repo) is in the same folder as the Python script. Make any necessary changes in the script regarding file paths, etc., and then run the script.
  - From `Thermal_CNT_0_25_1.96.log.lammps`, a .csv file (`Thermal_CNT_0_25_1.96.csv`) will be created
  - From `Thermal_CNT_0_25_1.96.log.lammps`, a PNG image (`Thermal_CNT_0_25_1.96_HeatFlux.png`) will be created


# [By Drew] Here are the next steps for calculating thermal conductivity:
1. Redo ~20 other simulations using the same LAMMPS input script, but with different random number seeds for the velocities. These are called “ensembles” in statistical physics.
2. Calculate the heat flux autocorrelation for each of these 20 simulations.
3. Average the autocorrelation for all simulations, for each time. This is <Q(t)Q(0)>
Time-integrate <Q(t)Q(0)>, and plot it as a function of integration time. The value that this integral levels off at will be the thermal conductivity, after we multiply by some constants according to the Green-Kubo formula:
