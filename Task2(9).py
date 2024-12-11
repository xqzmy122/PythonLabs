str = "Это был огромный, в два обхвата дуб, c обломанными ветвями и c обломанной корой"
dict = {}
splitted_str = str.split()

def fill_dict(list):
    for el in list:
        el_length = len(el)
        dict[el] = el_length
    
    print(dict)

fill_dict(splitted_str)
