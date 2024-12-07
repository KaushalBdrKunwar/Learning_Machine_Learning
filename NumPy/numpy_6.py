import numpy as np

#Mathematical operations on a np array.

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1 + list2) # its concatinated

a = np.random.randint(0,10,(3,3))
b = np.random.randint(10,20,(3,3))
print(a)
print(b)
print(a+b) # addition of matrix
print(a-b)
print(a*b)
print(a/b)

# or

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))