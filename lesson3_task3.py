numbers = (input("Введите 3 числа через пробел: "))
my_list = numbers.split()


def max_numbers(x, y, z):
    if x <= y and x <= z:
        print("Сумма двух наибольших чисел - ", z + y)
    elif y <= x and y <= z:
        print("Сумма двух наибольших чисел - ", x + z)
    elif z <= x and z <= y:
        print("Сумма двух наибольших чисел - ", x + y)


max_numbers(int(my_list[0]), int(my_list[1]), int(my_list[2]))
