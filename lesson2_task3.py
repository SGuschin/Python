num_month = int(input("Введите номер месяца : "))
num_year = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in range(len(num_year)):
    if num_month == num_year[i]:
        if i < 3:
            print("Зима")
            break
        elif i < 6:
            print("Весна")
            break
        elif i < 9:
            print("Лето")
            break
        print("Осень")
d = {"Зима": [12, 1, 2],
     "Весна": [3, 4, 5],
     "Лето": [6, 7, 8],
     "Осень": [9, 10, 11]}

for i in d.keys():
    if num_month in d[i]:
        print(i)
        break
