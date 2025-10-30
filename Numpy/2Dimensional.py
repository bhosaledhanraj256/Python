import numpy as np

# Create a 2D array (matrix)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D Array:\n", arr2)

# Basic operations
print("Shape:", arr2.shape)
print("Row-wise sum:", np.sum(arr2, axis=1))
print("Column-wise sum:", np.sum(arr2, axis=0))
print("Transpose:\n", arr2.T)
