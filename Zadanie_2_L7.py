from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def raschet(self):
        pass

class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def raschet(self):
        return f'Rashod sostavit: {2 * self.h + 0.3} m.'


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def raschet(self):
        return f'Rashod sostavit: {self.v / 6.5 + 0.5} m.'

my_suit = Suit(1.6)
my_coat = Coat(44)


print(my_suit.raschet)
print(my_coat.raschet)
