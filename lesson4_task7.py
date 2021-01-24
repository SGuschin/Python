from math import factorial

n = int(input("Введите значение n: "))


def new_generator():
    for i in range(1, n + 1):
        z = factorial(i)
        yield z


for el in new_generator():
    print(el)
