with open('lesson5_task5.txt', 'w') as file:
    file.write('1 2 3 4 5 110 56.05')
with open('lesson5_task5.txt', 'r') as file:
    numbers = file.readlines()
    print(numbers)
    numbers = numbers[0].split(' ')
    s = 0
    for x in numbers:
        s += float(x)
    print(s)

