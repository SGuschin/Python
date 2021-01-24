from functools import reduce


def my_funk(num_1, num_2):
    return num_1 * num_2


my_list = []
new_list = [x for x in range(100, 1001) if x % 2 == 0]
print(new_list)
print(reduce(my_funk, new_list))
