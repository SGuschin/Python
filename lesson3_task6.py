def int_func(s):
    s = s[0].upper() + s[1:]
    return s


str1 = input("Введите строку : ")
lst = str1.split()
str1 = ""
for l in lst:
    str1 += int_func(l) + " "
print(str1)
