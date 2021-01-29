text = ''
with open('lesson5_task4.txt', encoding='utf-8') as file:
    lst = file.readlines()
    print(lst)
    a = text.join(lst)
    print(a)
with open('lesson5_task44.txt', 'w') as file:
    for line in lst:
        if '1' in line:
            a = a.replace('One', 'Один')
        elif '2' in line:
            a = a.replace('Two', 'Два')
        elif '3' in line:
            a = a.replace('Three', 'Три')
        elif '4' in line:
            a = a.replace('Four', 'Четыре')
        file.writelines(a)
