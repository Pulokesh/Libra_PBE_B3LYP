import numpy as np
from scipy.sparse import csc_matrix
import sys
import os

def average_npz_files(npz_files, output_file):
    sum_matrix = None
    count = 0
    
    for npz_file in npz_files:
        # Load each NPZ file
        data = np.load(npz_file)
        
        # Check if the necessary keys are present
        if {'data', 'indices', 'indptr', 'shape'}.issubset(data.files):
            # Reconstruct the sparse matrix using CSC format
            sparse_matrix = csc_matrix((data['data'], data['indices'], data['indptr']), shape=data['shape'])
            
            # Convert to a dense matrix
            dense_matrix = sparse_matrix.todense()
            print("Diagonal elements of ", np.diagonal(dense_matrix))
            
            # Initialize sum_matrix on first iteration
            if sum_matrix is None:
                sum_matrix = dense_matrix
            else:
                sum_matrix += dense_matrix  # Sum up matrices
            
            count += 1
        else:
            print(f"File {npz_file} does not contain the necessary keys.")
    
    # Calculate the average
    if count > 0:
        average_matrix = sum_matrix / count

        # Save the average matrix to a text file
        np.savetxt(output_file, average_matrix, fmt='%.10f')
        print(f"Average matrix has been written to {output_file}")

        # Print the average matrix
        print("Average matrix:")
        print(average_matrix)

        # Print the average matrix diagonal elements
        diagonal_elements = np.diagonal(average_matrix)
        print("Diagonal elements of the average matrix:")
        print(diagonal_elements)
    else:
        print("No valid NPZ files provided.")

if __name__ == "__main__":
    # Check if the user provided the correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <output_txt_file> <input_npz_files...>")
    else:
        # Get the output TXT file path and list of input NPZ file paths
        output_file_path = sys.argv[1]
        npz_files = sys.argv[2:]

        # Call the function with the provided paths
        average_npz_files(npz_files, output_file_path)

