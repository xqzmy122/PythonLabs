list = []

str_amount = int(input("str amount: "))

for i in range(str_amount):
    new_str = input("enter str to the list: ")
    list.append(new_str)

def sort_list(list):
    sorted_list = sorted(list, key = lambda x: x.lower())
    print(sorted_list)

sort_list(list)