import matplotlib.pyplot as plt
import numpy as np
import random 

matrix = np.random.randint(0, 100, size=(10,10))

for i in range(len(matrix)): 
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

fig, ax = plt.subplots()
plt.imshow(matrix, cmap='viridis')
plt.colorbar()
ax.set_title("graphic 4")
plt.show()
