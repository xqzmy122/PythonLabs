number = int(input("Enter the number: "))

def reverse_output(number):
    iter_count = number  
    while iter_count >= 1:  
        print(iter_count)   
        iter_count -= 1    

reverse_output(number)
