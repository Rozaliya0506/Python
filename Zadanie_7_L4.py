def my_gen(num):
    current = 1
    for el in range(1, num + 1):
        current *= el
        yield current

n = 5
for i in my_gen(n):
    print(f'= {i}')
