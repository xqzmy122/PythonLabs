import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5, 40)
y1 = []
y2 = []
const = 2

def function1(list1, list2):
    for i in range(len(list1)):
        value = 2*((list1[i]**2)**2)
        y1.append(value)

    return y1

def function2(list1, list2, const):
    for i in range(len(list1)):
        value = (list1[i] ** 2) + const
        y2.append(value)

    return y1

x.sort()
function1(x,y1)
function2(x,y2, const)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x,y1, label='first_func')
ax2.plot(x,y2, label='second_func', color='r')
ax1.set_title('functions', fontsize=16)
ax1.set_ylabel('y values', fontsize=12, color='r')
ax2.set_ylabel('y2 values', fontsize=12, color='b')
ax1.legend(loc='lower right')
ax2.legend(loc='lower left') #question

selected_x = 2
selected_y = (selected_x ** 2) + const
arrowprops = {'arrowstyle': '->'}

ax1.annotate('super important point',
            xy = (selected_x,selected_y + 30),
            xytext = (selected_x + 1.5,selected_y + 70),
            arrowprops=arrowprops)

plt.legend()
plt.show()