with open('lesson5_task2.txt', encoding='utf-8') as file:
    text = file.readlines()
    size = len(text)
    print(f'В файле - {size} cтроки')
    num_1 = 0
    for i in text:
        lst = i.split()
        numbers_line = len(lst)
        num_1 += 1
        print(f'В {num_1} строке {numbers_line} слова')
