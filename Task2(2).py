list = []

for element in range(3):
    num = int(input("enter the number: "))
    list.append(num)    

def find_index(list):
    min_value = 100000000
    for i in list:
        if (i < min_value):
            min_value = i

    iter = 0
    index = -1

    for i in list:
        if (list[iter] == min_value):
            index = iter
        iter += 1

    print(index)


find_index(list)


