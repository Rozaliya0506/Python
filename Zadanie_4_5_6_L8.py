class WarehouseTech:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.my_warehouse_full = []
        self.my_warehouse = []
        self.my_unit = {'Type of tech': self.name, 'Numbers': self.quantity}

    def __str__(self):
        return f'{self.name} numbers {self.quantity}'

    def priem(self):

        try:
            unit = input(f'Write a name of tech ')
            unit_q = int(input(f'Write a number '))
            unique = {'Type of tech': unit, 'Numbers': unit_q}
            self.my_unit.update(unique)
            self.my_warehouse.append(self.my_unit)
            print(f'In stock -\n {self.my_warehouse}')
        except:
            return f'You write incorrect'

        print(f'If you want to stop - *, if you want to continue - Enter')
        q = input(f'......')
        if q == '*':
            self.my_warehouse_full.append(self.my_warehouse)
            print(f'The all in stock -\n {self.my_warehouse_full}')
            return f'Quit'
        else:
            return WarehouseTech.priem(self)


class Printer(WarehouseTech):
    def to_print(self):
        print('Printer makes you to your document')


class Scanner(WarehouseTech):
    def to_scan(self):
        print('Scanner makes a copy of your document and save on PC')


class Copier(WarehouseTech):
    def to_copier(self):
        print('Copier makes copy of your document and give to you document')

tech_1 = Printer('a', 10)
tech_2 = Scanner('b', 13)
tech_3 = Copier('c', 26)
print(tech_1.to_print())
print(tech_2.to_scan())
print(tech_3.to_copier())
print(tech_1.priem())

