import matplotlib.pyplot as plt
import numpy as np

values = [24, 17, 1000, 21, 35]
labels = ["Ford", "Toyota", "BMW", "AUDI", "Jaguar"]

fig, ax = plt.subplots()
ax.pie(values, labels=labels)
ax.axis("equal")

plt.show()