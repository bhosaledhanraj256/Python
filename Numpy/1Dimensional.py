import numpy as np

# Create a 1D array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# Basic operations
print("Shape:", arr1.shape)
print("Sum:", np.sum(arr1))
print("Max:", np.max(arr1))
print("Index of 30:", np.where(arr1 == 30))
