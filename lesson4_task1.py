import sys

first_param, second_param, third_param = sys.argv[1:]

print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)

result = (int(first_param) * int(second_param)) + int(third_param)
print(f'Заработная плата сотрудника равна - {result}')
