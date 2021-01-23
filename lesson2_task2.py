str_1 = input("Введите числа через пробел: ")
my_list = str_1.split()
k = int(len(my_list) / 2) * 2
for i in range(0, k-1, 2):
    #t = my_list[i]
    #my_list[i] = my_list[i+1]
    #my_list[i+1] = t
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)
