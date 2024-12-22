import os
import glob
import numpy as np
import scipy.sparse as sp
from libra_py import units, data_stat, influence_spectrum
import matplotlib.pyplot as plt
from liblibra_core import *
from libra_py.workflows.nbra import step3
import libra_py.packages.cp2k.methods as CP2K_methods



#%matplotlib notebook
params = {"path_to_energy_files": "res-mb-sd-DFT", "dt": 1.0, 
          "prefix": "Hvib_sd_", "suffix": "_re", "istep": 0, "fstep": 6}



#%matplotlib notebook
params = {"path_to_all_pdos": '../TEST4/all_pdosfiles', "atoms": [[1,2] , ['Ti', 'O']],
          "orbitals_cols": [[3], range(4,7), range(7,12), range(12,19)], "orbitals":  ['s','p','d','f'],
          "npoints": 4000, "sigma": 0.05, "shift": 2.0}

ave_energy_grid, homo_energy, ave_pdos_convolved, pdos_labels, ave_pdos_convolved_total = CP2K_methods.pdos(params)
print(pdos_labels)
for i in range(len(pdos_labels)):
    pdos_label = pdos_labels[i]
    plt.plot(ave_energy_grid-homo_energy, ave_pdos_convolved[i], label=pdos_label)
plt.plot(ave_energy_grid-homo_energy, ave_pdos_convolved_total, color='black', label='Total')
plt.legend()
plt.xlim(-4,4)
plt.ylabel('pDOS, 1/eV')
plt.xlabel('Energy, eV')
plt.title('TiO$_2$, 300 K')
plt.tight_layout()


plt.savefig('PDOS_TiO2.jpg', dpi=600)
print("Done completing SD_MB_NACS")
