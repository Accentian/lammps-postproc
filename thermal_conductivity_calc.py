import os, sys
import shutil
import numpy as np
import matplotlib.pyplot as plt

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

    col_check_str = '   Step          Temp       c_myFlux[1]  '
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

    ## Array for timestep converted to picosecond
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

    print(ps_arr)

    ## 1 row, 2 column of graphs for temperature for subplots
#     fig, axes = plt.subplots(1, 2, figsize = [15,4])

#     axes[0].plot(ps_arr, col_flux,label="temperature",c="r")
#     axes[0].set_title('Heat Flux vs Time')
#     axes[0].set_xlabel('MD Time (ps)')
#     axes[0].set_ylabel('Heat Flux')
#     axes[0].yaxis.get_ticklocs(minor=True)
#     axes[0].minorticks_on()

    plt.title("Heat Flux vs Time")
    plt.plot(ps_arr, col_flux, color="red")
    plt.xlabel('Time (ps)')
    plt.ylabel('Heat flux (eV/A^2/ps)')

    ## Create a PNG of the graphs and save it
    png_name = f'{file_stem}_HeatFlux.png'
    plt.tight_layout()
    plt.savefig(png_name, transparent=True) ## Set to True for transparent images

    ## Show and close the graphs. Required for normal scripts
    plt.show()
    plt.close()
