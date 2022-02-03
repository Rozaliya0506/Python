from itertools import cycle, count

for el in count(5):
    print(el)
    if el > 25:
        break

my_list = [0, 2, 5, 7, 10]
num = 1
for el in cycle(my_list):
    print(el)
    num += 1
    if num > 20:
        break

