result = float(input("Введите результат пробежки за первый день: "))
final = float(input("Сколько км вы хотели бы преодолевать за день: "))
day = 0
while result <= final:
    day += 1
    Magnification = float(result * 0.1)
    result = float(result + Magnification)
    print(f'День номер {day}. Вы пробежали {result:.2f}')