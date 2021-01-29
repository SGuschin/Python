with open('lesson5_task3.txt', encoding='utf-8') as file:
    text = file.readlines()
    print(text)
    d = {}
    for i in text:
        lst = i.split()
        d[lst[0]] = lst[1]
    # print(d)
    Sum = 0
    for m in d.keys():
        Sum += float(d[m])
        if float(d[m]) < 20000:
            print(f'{m} имеет зарплату меньше 20т.р.')
    average = Sum / len(d)
print(f'{average:.2f}')
