import matplotlib.pyplot as plt
import numpy as np
import random 

groups = [f"P{i}" for i in range(5)]
counts = np.random.randint(3, 10, len(groups))

fig, ax = plt.subplots()
ax.set_title("graphic 5")
plt.barh(groups, counts, color="green")
plt.show()
