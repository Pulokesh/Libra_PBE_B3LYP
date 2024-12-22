import os
import glob
import numpy as np
import scipy.sparse as sp
from libra_py import units, data_stat, influence_spectrum
import matplotlib.pyplot as plt
from liblibra_core import *
from libra_py.workflows.nbra import step3
import libra_py.packages.cp2k.methods as CP2K_methods


print("done Testing")

params_ks = {
              'lowest_orbital': 24-1, 'highest_orbital': 24+1, 'num_occ_states': 2, 'num_unocc_states': 1,
              'use_multiprocessing': True, 'nprocs': 40, 'time_step': 1.0, 'es_software': 'cp2k',
              'path_to_npz_files': os.getcwd()+'/../step2/res',
              'logfile_directory': os.getcwd()+'/../step2/all_logfiles',
              'path_to_save_ks_Hvibs': os.getcwd()+'/res-ks-DFT',
              'start_time': 0, 'finish_time': 6,
            }

# For KS orbitals
step3.run_step3_ks_nacs_libint(params_ks)
print("Done completing KS_NACS")
#'''
params_mb_sd = {
          'lowest_orbital': 24-1, 'highest_orbital': 24+1, 'num_occ_states': 2, 'num_unocc_states': 1,
          'isUKS': 0, 'number_of_states': 2, 'tolerance': 0.0, 'verbosity': 0, 'use_multiprocessing': True, 'nprocs': 40,
          'is_many_body': False, 'time_step': 1.0, 'es_software': 'cp2k',
          'path_to_npz_files': os.getcwd()+'/../step2/res',
          'logfile_directory': os.getcwd()+'/../step2/all_logfiles',
          'path_to_save_sd_Hvibs': os.getcwd()+'/res-mb-sd-DFT',
          'outdir': os.getcwd()+'/res-mb-sd-DFT', 'start_time': 0, 'finish_time': 4, 'sorting_type': 'energy',
         }

step3.run_step3_sd_nacs_libint(params_mb_sd)

print("Done completing SD_MB_NACS")
#'''
