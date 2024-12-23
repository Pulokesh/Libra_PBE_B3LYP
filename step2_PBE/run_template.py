import os
import sys
import libra_py.packages.cp2k.methods as CP2K_methods
from libra_py.workflows.nbra import step2


path = os.getcwd()
params = {}

# number of processors
params['nprocs'] = 40

# The mpi executable
# The executable can be srun, mpiexe, mpirun, etc. If you're using slurm for job submission and
# you want to use Intel compiled version of CP2K, use 'srun' as your executable. Since we are using GNU-based
# executable, we use the OpenMP 'mpirun'
#params['mpi_executable'] = 'mpirun'
params['mpi_executable'] = 'srun'

# CP2K executable 
# You can choose any of these compiled versions but please note that you should first load all the required 
# dependencies in the "submit" file and not here. Also, note that the Intel compiled version can obly run on specific nodes on UB CCR.
# Other users need to adapt this based on their own environments.

# CP2K v23.1 compiled with GNU compilers v11.2.0 + Intel MKL v2020.2 + OpenMP v4.1.1, Runs on all general compte and faculty cluster nodes. Other dependencies for this compiled version are:
# DFLAGS = -D__parallel  -D__MKL -D__FFTW3  -D__SCALAPACK -D__FFTW3  -D__LIBINT -D__LIBXC -D__HAS_smm_dnn -D__COSMA -D__ELPA  -D__QUIP -D__GSL -D__PLUMED2 -D__HDF5 -D__LIBVDWXC -D__SPGLIB -D__LIBVORI -D__SPFFT -D__SPLA
#params['cp2k_exe'] = 'cp2k.psmp'
params['cp2k_exe'] = 'cp2k.popt'

# Leave this part for Libra
params['istep'] = 
params['fstep'] = 

# Lowest and highest orbital, Here HOMO is 160
params['lowest_orbital'] = 160-10
params['highest_orbital'] = 160+11
#params['lowest_orbital'] = 24-10
#params['highest_orbital'] = 24+11

# extended tight-binding calculation type
params['isxTB'] = False
# unrestricted spin configuration
params['isUKS'] = False
# Periodic calculations flag
params['is_periodic'] = True
# Set the cell parameters for periodic calculations

if params['is_periodic']:
    params['A_cell_vector'] = [15.92750000, 0.00000000, 0.00000000]
    params['B_cell_vector'] = [-7.96450770, 13.78648425, 0.00000000]
    params['C_cell_vector'] = [-0.00010396, 0.00006001, 29.78360000]
    params['periodicity_type'] = 'XYZ'
    # Set the origin for generating the translational vectors (for creating Bloch type functions)
    origin = [0,0,0]
    tr_vecs = params['translational_vectors'] = CP2K_methods.generate_translational_vectors(origin, [2,2,2],
                                                                                            params['periodicity_type'])
    
    print('The translational vectors for the current periodic system are:\n')
    print(tr_vecs)
    print(F'Will compute the S^AO between R(0,0,0) and {tr_vecs.shape[0]+1} translational vectors')

# The AO overlaps in spherical or Cartesian coordinates
params['is_spherical'] =  True
# Remove the molden files, which are large files for some systems, 
# after the computaion is done for tha system
params['remove_molden'] = True

# Cube visualization using VMD
# For the TiO2 unit cell we do not visualize the cube files, 
params['cube_visualization'] = False
if params['cube_visualization']:
    # The only parts that we will change in this template are loading the cubes and rendering the images.
    params['vmd_input_template'] = '../vmd_cube_template.tcl'
    params['states_to_plot'] = [24,25]
    params['plot_phase_corrected'] = True
    params['vmd_exe'] = 'vmd'
    params['tachyon_exe'] = '/util/academic/vmd/1.9.2/lib/vmd/tachyon_LINUXAMD64'
    params['x_pixels'] = 1024
    params['y_pixels'] = 1024
    params['image_format'] = 'bmp'
    params['remove_cube'] = True
    params['all_images'] = path + '/../all_images'

# The results are stored in this folder
params['res_dir'] = path + '/../res'
params['all_pdosfiles'] = path + '/../all_pdosfiles'
params['all_logfiles'] = path + '/../all_logfiles'
# If the xTB calculations are needed, we need an OT procedure 
params['cp2k_ot_input_template'] = path + '/../es_ot_temp.inp'
params['cp2k_diag_input_template'] = path + '/../es_diag_temp.inp'
# The trajectory xyz file path
# Note that since it will be run in one of the jobs folders
# we need to put one more .. so that it can recognize the file
params['trajectory_xyz_filename'] = path + '/../SiH_GeH-pos-1.xyz'



step2.run_cp2k_libint_step2(params)
