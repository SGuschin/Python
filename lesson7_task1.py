class Matrix:
    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        answer = ' '
        if len(self.matrix) == len(other.matrix):
            for line_1, line_2 in zip(self.matrix, other.matrix):
                if len(line_1) != len(line_2):
                    return 'Something go wrong! Check shape'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, sum_line)) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[2, 4], [6, 8], [10, 12], [14, 16]])
matrix_2 = Matrix([[1, 3], [5, 7], [9, 11], [13, 15]])
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)
