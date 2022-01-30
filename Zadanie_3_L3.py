def my_func(num_1,num_2,num_3):
    sum_a = num_1 + num_2 + num_3
    return sum_a - min(num_1, num_2, num_3)

n_1 = int(input("Number 1 = "))
n_2 = int(input("Number 2 = "))
n_3 = int(input("Number 3 = "))
result = my_func(n_1, n_2, n_3)
print(result)
