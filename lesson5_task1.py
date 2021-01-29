with open('lesson5_task1.txt', 'w') as file:
    while True:
        line = input('Введите строку: ')
        if line == '':
            break
        f.write(line + '\n')
