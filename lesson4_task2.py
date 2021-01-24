#def my_func(lst):
#    for i in range(len(lst) - 1):
#        if lst[i] > lst[i - 1]:
#            yield lst[i]


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#new_list = [x for x in my_func(my_list)]
#print(new_list)
new_list = [my_list[x] for x in range(len(my_list)) if my_list[x] > my_list[x - 1]]
print(new_list)
