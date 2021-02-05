class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num // rows)]) + '\n' + '*' * (self.num % rows)

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return 'Sum is - ' + str(self.num + other.num)

    def __sub__(self, other):
        return self.num - other.num if self.num - other.num > 0 \
            else 'Вычитание невозможно'

    def __mul__(self, other):
        return 'Multiply is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return ' Truediv is - ' + str(round(self.num / other.nims))


cell_1 = Cell(20)
cell_2 = Cell(44)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(20))
