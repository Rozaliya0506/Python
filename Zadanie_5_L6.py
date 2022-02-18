class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start to draw')

class Pen(Stationery):

    def draw(self):
        print(f'Start to draw with pen - {self.title}')

class Pencil(Stationery):

    def draw(self):
        print(f'Start to draw with pencil - {self.title}')

class Handle(Stationery):

    def draw(self):
        print(f'Start to draw with handle - {self.title}')

ex_1 = Stationery('main')
ex_2 = Pen('Red')
ex_3 = Pen('Green')
ex_4 = Pencil('Grey')
ex_5 = Pencil('Blue')
ex_6 = Handle('Black')
ex_7 = Handle('White')

ex_1.draw()
ex_2.draw()
ex_3.draw()
ex_4.draw()
ex_5.draw()
ex_6.draw()
ex_7.draw()
