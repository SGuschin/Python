from abc import ABC, abstractmethod


class Clothers(ABC):
    def __init__(self, things):
        self.things = things

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothers):

    @property
    def calculate(self):
        return round((self.things / 6.5) + 0.5)


class Suit(Clothers):

    @property
    def calculate(self):
        return round((2 * self.things ) + 0.3)


my_coat = Coat(45)
my_suit = Suit(179)
print(my_coat.calculate)
print(my_suit.calculate)
print(my_coat.calculate + my_suit.calculate)
