import sys
import numpy as np
from scipy.sparse import csc_matrix

# Function to convert an NPZ file with a sparse matrix into a dense .txt file
def npz_to_txt(npz_file, output_file):
    # Load the NPZ file
    data = np.load(npz_file)
    
    # Check for required keys
    if {'data', 'indices', 'indptr', 'shape'}.issubset(data.files):
        # Reconstruct the sparse matrix using CSC format
        sparse_matrix = csc_matrix((data['data'], data['indices'], data['indptr']), shape=data['shape'])
        
        # Convert to a dense matrix
        dense_matrix = sparse_matrix.todense()
        
        # Save the dense matrix to a text file
        np.savetxt(output_file, dense_matrix, fmt='%.10f')
        print(f"Dense matrix has been written to {output_file}")
    else:
        print("The NPZ file does not contain the necessary keys to form a sparse matrix.")

# Specify the input NPZ file and the output text file
npz_file_path = sys.argv[1]
output_file_path = sys.argv[2]
#npz_file_path = sys.argv[1]+".npz"
#output_file_path = npz_file_path.split('/')[1]+".txt"
#npz_file_path = "res/St_ks_0.npz"
#output_file_path = "St_ks_0_dense_matrix.txt"

# Call the function
npz_to_txt(npz_file_path, output_file_path)

