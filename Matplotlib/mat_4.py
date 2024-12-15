import matplotlib.pyplot as plt
import numpy as np

#Parabola
x = np.linspace(-10,10,20)
y = x**2

#Bar plot
fig = plt.figure()
ax = fig.add_axes([0,0,0.9,0.9])
languages = ['English', 'French', 'Spanish', 'Latin', 'German']
people = [100, 50, 150, 40, 70]
ax.bar(languages, people)
plt.xlabel('Languages')
plt.ylabel('Number of People')
print(plt.show())