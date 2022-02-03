def sum_num(nums, stop_w):
    nums_str = nums.split(' ')
    sum_n = 0
    for el in nums_str:
        if el == stop_w:
            break
        sum_n += int(el)
    return sum_n

stop = '*'
finish = False
a = 0
while not finish:
    user_input_nums = input("Write numbers:")
    a += sum_num(user_input_nums,stop)
    finish = stop in user_input_nums
    print(f'Result = {a}')
