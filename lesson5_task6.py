my_dict = dict()
with open('lesson5_task6.txt', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    splitted_line = line.split()
    subject = splitted_line[0]
    sum_num = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
    my_dict[subject[:-1]] = sum_num
print(my_dict)
