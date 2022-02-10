class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

sotrudnik = Position('Rozaliya', 'Baltacheva','Engeneer', 50000, 25000)

print(sotrudnik.name)
print(sotrudnik.surname)
print(sotrudnik.get_full_name())
print(sotrudnik.get_total_income())
