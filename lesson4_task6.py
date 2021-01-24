from itertools import count, cycle

for el in count(start=3, step=1):
    if el > 10:
        break
    print(el)

num_1 = 0
sentence = ["Поели, можно и поспать", "Поспали, можно и поесть"]
for el in cycle(sentence):
    if num_1 > 10:
        break
    print(el)
    num_1 += 1

