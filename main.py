import math

x = float(input("enter x value: "))
b = float(input("enter b value: "))

def first_condition(x,b):
    y = math.exp((x**2) - abs(b))
    print(y)
    print("1 condition")

def second_condition(x,b):
    y = math.sqrt(abs((x ** 2) + b))
    print(y)
    print("2 condition")

def third_condition(x):
    y = 2*((x**2)**2)
    print(y)
    print("3 condition")

xb = x*b
if (xb > 0.5 and xb < 10):
    first_condition(x,b)
elif (xb > 0.1 and xb < 0.5):
    second_condition(x,b)
else:
    third_condition(x)


  


