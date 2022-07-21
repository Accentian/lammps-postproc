'''
Collabrated with Drew Rohskopf
'''

from numpy import *
import os, sys
import shutil
import numpy as np
import matplotlib.pyplot as plt

## Calculates the correlation
def estimated_autocorrelation(x):
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = np.correlate(x, x, mode = 'full')[-n:]
    result = r/(variance*(np.arange(n, 0, -1)))
    return result

## Takes in files that has .lammps in their names. Limited to only the folder this scirpt is in.
all_the_log_files = [f for f in os.listdir() if f.endswith('.lammps') and not os.path.isdir(f)]

store_numpy_arrays = []

## Loops through any files containing .lammps
for i, log_file in enumerate(all_the_log_files):
    print(log_file)
    file_stem = log_file.replace('.log.lammps','')

    ## Get the text from the log file
    with open(log_file, 'r') as f:
        txt = f.readlines()

    col_check_str = '   Step          Temp       c_myFlux[3]  '
    end_check_str = 'Loop time of '
    columns = None
    start_idx, end_idx = 0, len(txt)

    ## If the code detects a particular line, begin reading the entire section below that until a certain point
    for line_idx, line in enumerate(txt):
        if col_check_str in line:
            columns = line.strip().split()
            start_idx = line_idx + 1
        if end_check_str in line and columns:
            end_idx = line_idx - 1


    data0 = txt[start_idx:end_idx + 1]
    data = [row for row in data0 if len(row.split()) == 3] ## Should the log.lammps be cut off early, remove cut off row
    columns_entry = None

    ## PRINT DEBUG
#     print(columns)
#     print(start_idx,end_idx)
#     print(data0[-1:])

    ## write the CSV file
    csv_name = f'{file_stem}.csv'
    with open(csv_name, 'w') as f:
        f.write(",".join(columns) + "\n")
        for start_idx in data:
            ## Check if the rows has all the columns. If it is missing all 14 columns, remove the entire row.
            ## Suggested by Drew Rohskopf
            columns_entry = start_idx.strip().split()
            line_length = len(columns_entry)
            if (line_length==3):
                f.write(",".join(columns_entry) + "\n")

    ## Create an array to store each elements from a column
    arr = np.array([[float(element) for element in row.split()] for row in data])
    store_numpy_arrays.append(arr)

    copy_arr = arr.copy()
    col_flux = copy_arr[:,2]

    ## List for timestep converted to picosecond
    ps_arr = []
    snapshots = 0

    ## PRINT DEBUG
    #print(col_flux)
    #print(col_step)

    ## Calculate timesteps into picoseconds
    for counter in data:
        picoseconds = 0.0005 * snapshots
        ps = round(picoseconds,8)
        ps_arr.append(ps)
        #print(ps)
        snapshots = snapshots + 5
    #print(ps_arr)
    ## Convert list to array.
    ps_arr = np.array(ps_arr)

    ## Plot heat flux vs time
    plt.figure() # creates a figure
    plt.title("Heat Flux vs Time")
    plt.plot(ps_arr, col_flux, color="red", label='Heat Flux')
    plt.xlabel('Time (ps)')
    plt.ylabel('Heat flux (eV/A^2/ps)')
    plt.savefig(f'{file_stem}_HeatFlux.png')
    ##DEBUG: Create a PNG of the graphs and save it
    #png_name = f'{file_stem}_Flux.png'
    #plt.savefig(png_name, transparent=True) ## Set to True for transparent images

    ## Calls estimated_autocorrelation
    ndat = len(ps_arr)
    autocor = estimated_autocorrelation(col_flux)
    minimum = min(autocor[0:int(ndat/2)])
    maximum = max(autocor[0:int(ndat/2)])
    #print(autocor[0])

    ## Overlay heat flux for autocorrelation vs. correlation time
    plt.figure() # creates a figure
    plt.plot(ps_arr, col_flux, color="red", label='Heat Flux')
    plt.xlabel('Time (ps)')
    plt.ylabel('Heat flux (eV/A^2/ps)')
    plt.savefig(f'{file_stem}_HeatFlux.png')

    plt.title("Heat Flux vs Time")
    plt.plot(ps_arr, autocor, label='Mean Flux')
    plt.xlabel('Time (ps)')
    plt.ylabel('Heat flux (eV/A^2/ps)')
    plt.xlim([0.0,ps_arr[-1]/2])
    #plt.ylim([minimum,maximum])
    #plt.tight_layout()
    #plt.show()
    plt.legend()
    plt.savefig(f'{file_stem}_AutoCorrelation.png')

    ## Time-integrate the autocorrelation and timestep
    integral_array = []

    time_indices = np.arange(1000,len(ps_arr),1000)
    for t in time_indices:
        integral = np.trapz(autocor[0:t], ps_arr[0:t])
        integral_array.append(integral)
    integral_array = np.array(integral_array) # integrated autocorrelations
    integral_times = ps_arr[time_indices] # times to plot integrated autocorrelations against

    ## Plot thermal conductivity accumulation vs. integration time
    plt.figure() # creates a figure
    plt.title("Thermal Conductivity Accumulation")
    plt.plot(integral_times, integral_array)
    plt.xlabel('Time (ps)')
    plt.ylabel('Heat flux (eV/A^2/ps)')
    plt.xlim([0.0,ps_arr[-1]/2])
    plt.savefig(f'{file_stem}_TCAccumulation.png')
    ## Show and close the graphs. Required for normal scripts
    plt.show()
    plt.close()
