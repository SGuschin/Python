second = int(input("Введите количество секунд: "))
hours1 = second // 3600
hours2 = second % 3600
minutes1 = hours2 // 60
minutes2 = hours2 % 60
seconds = minutes2
print(f'Получилось: {hours1} часов, {minutes1} минут, {seconds} секунд')

