new_list = []
old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
[new_list.append(x) for x in old_list if x not in new_list]
print(new_list)
