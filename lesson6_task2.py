class Road:

    def __init__(self, length, width, mass, heigth):
        self._length = length
        self._width = width
        self._mass = mass
        self._heigth = heigth

    def calc(self):
        print(f'{self._length}м * {self._width}м * {self._mass}кг * {self._heigth}см = '
              f'{(self._length * self._width * self._mass * (self._heigth * 0.01)) / 1000} т')


my_mass = Road(20, 5000, 25, 5)
my_mass.calc()
