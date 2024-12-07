#Initial Placeholders in arrays.

import numpy as np

x = np.zeros((4,5))
print(x)

#create a numpy array of ones.
y = np.ones((3,3))
print(y)

# array of a particular value.

z = np.full((5,4),5)
print(z)

#Create an identity matrix.
#No.of rows and columns should be equal.
l = np.eye(4)
print(l)

#create a numpy array with random values.

b = np.random.random((3,4))
print(b)

# crate random values array with integers.

c = np.random.randint(10,100,(3,5))
print(c)

#create array of evenly spaced values.
d = np.linspace(10,30,5)
print(d)