import matplotlib.pyplot as plt
import numpy as np

#Parabola
x = np.linspace(-10,10,20)
y = x**2
plt.plot(x,y)
print(plt.show())
plt.plot(x,y, 'r+')
print(plt.show())
plt.plot(x,y,'g.')
print(plt.show())

#Multiple lines in a single plot.
plt.plot(x, np.sin(x), 'g-')
plt.plot(x, np.cos(x), 'r--')
print(plt.show())

