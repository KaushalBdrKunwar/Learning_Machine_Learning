import matplotlib.pyplot as plt
import numpy as np

#PIE CHART

fig1 = plt.figure()
ax = fig1.add_axes([0,0,1,1])
languages = ['English', 'French', 'Spanish', 'Latin', 'German']
people = [100, 50, 150, 40, 70]
ax.pie(people, labels=languages, autopct='%1.1f%%')
print(plt.show())

#Scatter PLOT

x = np.linspace(0,10,30)
y = np.sin(x)
z = np.cos(x)
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.scatter(x,y,color='g')
ax.scatter(x,z,color='b')
print(plt.show())