import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sine value')
plt.title('sine wave')
print(plt.show())
