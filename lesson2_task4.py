str1 = input("Введите строку : ")
lst = str1.split()
i = 1
for s in lst:
    print(i, end="\t")
    i += 1
    print(s if len(s) <= 10 else s[:11])