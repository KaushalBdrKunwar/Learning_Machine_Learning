#Importing matplotlib library
import matplotlib.pyplot as plt

#Import numpy to get data for our plots
import numpy as np

x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)

print(x)
print(y)
print(z)

#ploting the data
#1. sine wave
plt.plot(x,y)
print(plt.show())

#2. cosine wave
plt.plot(x,z)
print(plt.show())