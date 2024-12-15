import matplotlib.pyplot as plt
import numpy as np

#3-D SCATTER PLOT
fig3 = plt.figure()
ax = plt.axes(projection='3d')
z = 20 * np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z,cmap='Blues')
print(plt.show())
