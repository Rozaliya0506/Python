def div_num(num_1, num_2):
    if num_2 == 0:
        return "Can't divide by zero"
    else:
        return num_1 / num_2

user_input_num_1 = int(input('Write a number: '))
user_input_num_2 = int(input('Write a number: '))
print(div_num(user_input_num_1, user_input_num_2))
