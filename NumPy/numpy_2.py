import numpy as np

#Difference between list and array.
list1 = [1,2,3,4,5]
print(list1)
print(type(list1))

np_array = np.array([1,2,3,4,5])
print(np_array)
print(type(np_array))

#Creating a 1 dim array
a = np.array([1,2,3,4])
print(a)
print(a.shape)

#2-D array
b = np.array([(1,2,3,4),(5,6,7,8)])
print(b)
print(b.shape)