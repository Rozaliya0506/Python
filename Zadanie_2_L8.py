class MyException(Exception):
    def __init__(self, num):
        self.num = num

try:
        a = input('Write a number:')
        b = input('Write a number:')
        c = int(a) / int(b)
        print('Number is correct')

except ZeroDivisionError:
    print('Please do not write a 0')
