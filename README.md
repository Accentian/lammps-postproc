# Uses Python in Jupyter Notebook or any IDE that supports Python

This repo contains a series of Python scripts designed to process data after a successful LAMMPS run.

  1. thermal_conductivity_calculations.ipynb (OUTDATED) - 
This Python code was created in Jupyter Notebook. It reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of `Step`, `Temp`, and `c_myFlux[1]` are located. It will then parse only the c_myFlux[1] column for thermal conductivity calculations.

  2. thermal_conductivity_calc.py (OUTDATED) - 
This Python script is identical to `thermal_conductivity_calculations.ipynb`. Ensure that the imports or Python environments for numpy and matplotlib.pyplot exists in order for the script to work. Like the first listing, the script reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of Step, Temp, and c_myFlux[1] are located. It will then parse only the `c_myFlux[1]` column for thermal conductivity calculations.

  3. v2thermal_conductivity_calc.py - 
This Python script is work in-progress script that's similar to `thermal_conductivity_calc.py`. Ensure that the imports or Python environments for numpy and matplotlib.pyplot exists in order for the script to work. Like the first listing, the script reads only log.lammps files that are in the same directory as this the script and creates a .csv file where the columns of Step, Temp, and c_myFlux[1] are located. It will then parse only the `c_myFlux[1]` column for thermal conductivity calculations using user defined functions.

    - extract the heat flux vs. time [Q(t)] from LAMMPS output
    - plot heat flux vs. time, along with the mean flux, to show that the system is in equilibrium
    - calculate heat flux autocorrelation, which is a measure of how long the heat flux signal stays correlated with itself

TO RUN THE SCRIPT(S) & RESULTS:
  - Make sure `Thermal_CNT_0_25_1.96.log.lammps` (or any log.lammps in this repo) is in the same folder as the Python script. Make any necessary changes in the script regarding file paths, etc., and then run the script.
  - From `Thermal_CNT_0_25_1.96.log.lammps`, a .csv file (`Thermal_CNT_0_25_1.96.csv`) will be created
  - From `Thermal_CNT_0_25_1.96.log.lammps`, several PNG image (`Thermal_CNT_0_25_1.96_AutoCorrelation.png, Thermal_CNT_0_25_1.96_HeatFlux.png, Thermal_CNT_1_19_1.53_TCAccumulation.png`) will be created

# [By Drew] These are the next steps to use your code to calculate thermal conductivity:

1. Do `N` simulations using the same input script, where N could be anywhere from 10-100 (more is better). These are called ???ensembles??? in statistical physics.
2. Use your code to calculate thermal conductivity accumulation vs. integration time for all ensembles.
3. Average TC accumulation for all ensembles.
4. That average is thermal conductivity, after we multiply by some constants according to the Green-Kubo formula (see Green-Kubo formula.png)

These steps are not implmented yet, but are straightforward using this code to calculate autocorrelation and accumulation.
