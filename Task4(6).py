import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random 


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100) 
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure(figsize=(10, 7)) 
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title('graphic 7')
ax.set_xlabel('X Axis') 
ax.set_ylabel('Y Axis') 
ax.set_zlabel('Z Axis')

plt.show()