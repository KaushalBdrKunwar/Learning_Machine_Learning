import numpy as np

#Analysing a numpy array

c = np.random.randint(10,90,(5,5))
print(c)

#array dimension
print(c.shape)

# number of dimension
print(c.ndim)

#number of elements in an array
print(c.size)

#checking the data type of values in the array.
print(c.dtype)