#!/bin/bash

#SBATCH --job-name CNT_0_25_1.96
#SBATCH --partition=batch
#SBATCH --time=5:00:00
#SBATCH --nodes=7
#SBATCH --account=fy220163         # WC ID

nodes=$SLURM_JOB_NUM_NODES
cores=$SLURM_CPUS_ON_NODE

module load intel/20.0.2.254
module load openmpi-intel/4.0
module load mkl/20.0.2.254
module unload anaconda3/5.2.0 && module load anaconda3/5.2.0

module list
#mpiexec --n $(($cores*$nodes)) /ascldap/users/bcma/
mpiexec --n $(($cores*$nodes)) /ascldap/users/bcma/lammps-develop/build/lmp -in CNT_0_25_1.96.in