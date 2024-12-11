set1= set()
set2 = set()

el_amount1 = int(input("amount 1: "))
el_amount2 = int(input("amount 2: "))

def fill_set(set, el_amount):
    for i in range(el_amount):
        el = input("enter element")
        set.add(el)

fill_set(set1, el_amount1)
fill_set(set2, el_amount2)

def find_diff(set1, set2):
    set = set1.symmetric_difference(set2)
    print(set)

find_diff(set1, set2)
