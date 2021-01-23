str_1 = input("Введите два числа через пробел: ")
my_list = str_1.split()
# print(my_list[0], my_list[1])


def numbers(num_1, num_2):
    return float(num_1 / num_2)


try:
    print(numbers(int(my_list[0]), int(my_list[1])))
except ZeroDivisionError:
    print("На ноль делить нельзя!")
