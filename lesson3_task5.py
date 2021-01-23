s = 0
fl = True
while fl:
    str1 = input("Выведите строку чисел, разделенных пробелом или $ : ")
    lst = str1.split()

    for i in lst:
        try:
            s += int(i)
        except ValueError:
            if i == "$":
                fl = False
                break

    print("сумма = " + str(s))
