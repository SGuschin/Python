my_list = [7, 5, 3, 3, 2]
print(my_list)
num = int(input("Введите число : "))
k = -1
for i in range(len(my_list)):
    if num >= my_list[i]:
        k = i
        break
if k != -1:
    my_list.insert(k, num)
else:
    my_list.append(num)
print(my_list)
