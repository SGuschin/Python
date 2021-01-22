profit = int(input("Введите прибыль вашего предприятия: "))
cost = int(input("Введите издержки вашего предприятия: "))
if profit > cost:
    print("Поздравляем, Ваше предприятие получает прибыль!")
    revenue = profit - cost
    profitability = (cost / revenue)
    print(f'Рентабельность предприятия = {profitability}')
    employee = int(input("Введите количество сотрудников: "))
    profit1 = int(profit/employee)
    print(f'Прибыль фирмы в расчёте на одного сотрудника = {profit1}')
elif profit < cost:
    print("К сожалению, Ваше предприятие несет убытки...")
