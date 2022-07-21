Collaborated with Drew Rohskopf. The `input` script calculates the heat flux.

# Here are the generalized step for the entire thing:

    1. Modify the LAMMPS scripts (particularly the .bash and .in) and make sure the bash script works with whatever system/cluster it is in 
    2. Run the scripts in LAMMPS [sbatch CNT_1_19_1.53.bash]
    3. Collect the output files (particularly log.lammps). There are also dump_production.xyz and dump_equilibration.xyz which can be visualized in OVITO
    4. Input log.lammps for v2thermal_conductivity_calc.py (have the log.lammps be in the same directory in the Python script) and run it
    5. A PNG image (see image of the graph attached to this) should be generated as well as a .csv file
