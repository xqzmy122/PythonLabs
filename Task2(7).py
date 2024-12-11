str1 = input("str1: ")
str2 = input("str2: ")

def is_anagram(str1, str2):
    str1.replace(' ', '').lower()
    str2.replace(' ', '').lower()

    return sorted(str1) == sorted(str2)

print(is_anagram(str1, str2))