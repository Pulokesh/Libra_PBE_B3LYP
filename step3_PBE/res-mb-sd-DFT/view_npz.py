import sys
from scipy import sparse
import numpy as np

fle_name=sys.argv[1]
sparse_array = sparse.load_npz(fle_name)
#sparse_array = sparse.load_npz('./res/E_ks_0.npz')
s=sparse_array.todense()
#print(sparse_array)
#print(sparse_array.toarray())
#print(np.diag(sparse_array.toarray()))
print(s)
print("length of data is= ",s.shape[0])
