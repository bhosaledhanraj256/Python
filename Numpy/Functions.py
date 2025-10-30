import numpy as np

# array creation function
a= np.array([1,2,3])
b= np.zeros ((2,3))
c= np.ones((2,2))
d= np.arange(0,10,2)
e= np.linspace(1,5,5)
f= np.eye(3) 

#  shape and reshape function
arr =np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)
print(arr.size)

reshaped = arr.reshape(3,2)
flattened = arr.flatten()

# mathemetical funtions 
arr= np.array([1,2,3,4])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.prod(arr))

# Axis based functions (for 2D, 3D)
arr2 = np.array([[1,2,3],
                 [4,5,6]])

print(np.sum(arr2, axis=0))    
print(np.sum(arr2, axis=1))    
# Element wise function 
arr = np.array([1,4,9,16])

print(np.sqrt(arr))            
print(np.square(arr))          
print(np.exp(arr))             
print(np.log(arr))             

# sortiong and searching functions 
arr = np.array([3,1,4,2])

print(np.sort(arr))            
print(np.argsort(arr))         
print(np.where(arr > 2))       
print(np.unique(arr))          

# matrix/ linear algebra functioins (for 2D)
A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

print(np.dot(A, B))            
print(np.transpose(A))         
print(np.linalg.inv(A))        
print(np.linalg.det(A))       
# Stacking combining arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a,b)))  
print(np.stack((a,b), axis=0))
print(np.vstack((a,b)))      
print(np.hstack((a,b)))      

# slicing and indexing
arr = np.array([10,20,30,40,50])
print(arr[1:4])               

arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr2[0,1])               
print(arr2[0:2, 1:3])          

# rashape 1D->2D->3D
x = np.arange(1,13)

x2 = x.reshape(3,4)           
x3 = x.reshape(2,3,2)         
