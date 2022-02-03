from functools import reduce
my_func = lambda a, b: a * b
my_list = reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])
print(my_list)
