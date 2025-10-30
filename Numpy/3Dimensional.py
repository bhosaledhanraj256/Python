import numpy as np

# Create a 3D array
arr3 = np.array([[[1, 2],
                  [3, 4]],
                 
                 [[5, 6],
                  [7, 8]]])
print("3D Array:\n", arr3)

# Basic operations
print("Shape:", arr3.shape)
print("Sum of all elements:", np.sum(arr3))
print("Sum along axis 0:\n", np.sum(arr3, axis=0))
print("Sum along axis 1:\n", np.sum(arr3, axis=1))
