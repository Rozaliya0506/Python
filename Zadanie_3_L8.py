class Spisok(Exception):

    def __init__(self, *args):
        self.my_spisok = []


    def proverka(self):

        while True:
            stop_s = '*'
            try:
                user_write =  input('Write a number:')
                if user_write == stop_s:
                    print(f'{self.my_spisok} \n')
                    break
                else:
                    user_int = int(user_write)
                    self.my_spisok.append(user_int)
                    print(f'{self.my_spisok} \n')
            except:
                print('You can write just a number! If you want to continue write Enter or press *')
                con_st = input('Write...')
                if con_st == stop_s:
                    print(f'Spisok is ready! {self.my_spisok}')
                    break



vvod = Spisok()
print(vvod.proverka())
