class Data:

    def __init__(self,dd_mm_yyyy):
        self.dd_mm_yyyy = dd_mm_yyyy

    @classmethod
    def get_numbers(cls, dd_mm_yyyy):
        data_str = []
        for el in dd_mm_yyyy.split('-'):
            data_str.append(el)
        dd = int(data_str[0])
        mm = int(data_str[1])
        yyyy = int(data_str[2])
        return f'Day is = {dd}; Month is = {mm}, Year is = {yyyy}'

    @staticmethod
    def proverka(day, month, year):
        if day >= 1 and day <= 31:
            if month >= 1 and month <=12:
                if year <= 2022:
                    return f'Data is correct'
                else:
                    return f'Year is not exist'
            else:
                return f'Month is not exist'
        else:
            return f'Day is not exist'


print(Data.get_numbers('10-02-2022'))
print(Data.proverka(32, 1, 2000))
print(Data.proverka(28, 5, 1987))
print(Data.proverka(31, 13, 2000))
print(Data.proverka(25, 1, 2023))







