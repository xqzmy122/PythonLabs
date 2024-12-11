import matplotlib.pyplot as plt
import numpy as np

# Данные для графиков
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Создание основного графика
fig, ax1 = plt.subplots()

# Первый график
ax1.plot(x, y1, 'r-', label='Синус')
ax1.set_xlabel('X')
ax1.set_ylabel('Синус', color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Создание второй оси Y
ax2 = ax1.twinx()
ax2.plot(x, y2, 'b-', label='Косинус')
ax2.set_ylabel('Косинус', color='b')
ax2.tick_params(axis='y', labelcolor='b')

# Добавление легенды
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Отображение графика
plt.title('Графики синуса и косинуса')
plt.show()