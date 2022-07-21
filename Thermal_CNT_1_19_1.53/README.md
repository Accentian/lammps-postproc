Collaborated with Drew Rohskopf. The `input` script calculates the heat flux.

# This file contains input files for running LAMMPS that can be used for post-processing using the Python script.

1. `Thermal_CNT_1_191.53` is a subdirectory containing all the files used or placed for references, including the outputs and post-proc results (PNG images).
2. `xdirection_Thermal_CNT_1_19_1.53` is a directory of the MD run in the x direction. The CNT's length is in the z direction hence why this directory exists to keep previous runs. It contains inputs, outputs, and post-proc results.


# Here are the generalized step for the entire thing:

    1. Modify the LAMMPS scripts (particularly the .bash and .in) and make sure the bash script works with whatever system/cluster it is in 
    2. Run the scripts in LAMMPS [sbatch CNT_1_19_1.53.bash]
    3. Collect the output files (particularly log.lammps). There are also dump_production.xyz and dump_equilibration.xyz which can be visualized in OVITO
    4. Input log.lammps for v2thermal_conductivity_calc.py (have the log.lammps be in the same directory in the Python script) and run it
    5. A PNG image (see image of the graph attached to this) should be generated as well as a .csv file
