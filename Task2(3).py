dict = {}

elements_amount = int(input("elements in dict: "))

def fill_dict(el, dict):
    for i in range(elements_amount):
        key = input("key")

        iter = 0
        for el in key:
            iter += 1
        dict[key] = iter

    print(dict) 

fill_dict(elements_amount, dict)



feqknfqenfqw