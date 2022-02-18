class Kletka:

    def __init__(self, kol):
        self.kol = kol

    def __add__(self, other):

        return f'Obschee kolichestvo kletok sostavlyaet: {self.kol + other.kol}'

    def __sub__(self, other):
        r = self.kol - other.kol
        if r < 0:
            return f'Raznost dvuh kletok menshe 0'
        else:
            return f'Raznost kletok sostavlyaet: {r}'

    def __mul__(self, other):

        return f'Proizvedenie dvuh kletok sostavlyaet: {self.kol * other.kol}'

    def __truediv__(self, other):

        r = self.kol // other.kol
        return f'Delenie dvuh kletok sostavlyaet: {r}'

    def make_order(self, kol_r):
        ryad = ""
        for el in range(self.kol // kol_r):
            ryad += '*' * kol_r + '\n'
        ryad += '*' * (self.kol % kol_r) + '\n'
        return ryad


kletka_1 = Kletka(107)
kletka_2 = Kletka(17)
print(kletka_1 + kletka_2)
print(kletka_1 - kletka_2)
print(kletka_2 - kletka_1)
print(kletka_1 * kletka_2)
print(kletka_1 / kletka_2)
print(kletka_1.make_order(10))

