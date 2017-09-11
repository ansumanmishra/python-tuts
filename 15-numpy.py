import numpy as np

# Create an np array
a = np.array([1, 2, 3, 4, 5])
print(a)

# Create an array using arange
a = np.arange(5)
print(a)

# Creating 2d array
a = np.array([[1,2,3],[4,5,6]])
print(a)

# Gets the rows & columns
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

# Doing mathematical operations for two or more arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x+y)

# Length of an np array
a = np.array([[1,2,3],[4,5,6]])
print(len(a)) # Prints 2

# Gives array dimensions
print(a.ndim) # Prints 2

# Get the count of all array elements
print(a.size) # Prints 6

# Gets the minimum value
print(a.min()) # Prints 1

# Gets the maximum value
print(a.max()) # Prints 6

# Sum of all elements of array
print(a.sum()) # Prints 21

# Sum array elements column wise
print(a.sum(axis=0)) # Prints [5,7,9]

# Sum array elements row wise
print(a.sum(axis=1)) # Prints [6,15]

# Avearage/Mean of array elements
print(a.mean())

# Gives the datatype
print(a.dtype) # Prints int64

# Prints datatype name
print(a.dtype.name) # Prints int64

# Creating array using arange and step
a =  np.arange(10,25,5)
print(a) # Here 5 is the step - Output is - [10 15 20]

''' Subsetting, Slicing, Indexing '''

