numbers = []
el_amount = int(input("el amount: "))

average = 0.0

def fill_list(list, el_amount):
    for i in range(el_amount):
        el = float(input("element: "))
        list.append(el)

fill_list(numbers, el_amount)

def find_average(list, avg):
    avg = sum(list)/len(list)
    
    return avg

average = find_average(numbers, average)

print(average)

def exclude(list, avg):
    ind = 0

    while ind < len(list):

        if(list[ind] < avg):
            list.remove(list[ind])
            continue
            
        ind += 1
    
    print(numbers)

exclude(numbers, average)