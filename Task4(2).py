import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

x2 = np.random.normal(7, 0.5, 50)
y2 = np.random.normal(7, 0.5, 50)

x3 = np.random.normal(10, 0.5, 50)
y3 = np.random.normal(10, 0.5, 50)


fig, ax = plt.subplots(figsize=(12,10))

ax.scatter(x1,y1, label='cluster 1', color='r')
ax.scatter(x2,y2, label='cluster 2', color='b')
ax.scatter(x3,y3, label='cluster 3', color='y')
ax.set_title('dot diagram with different colors for clusters')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.legend()
plt.show()