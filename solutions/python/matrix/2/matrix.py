class Matrix:
    def __init__(self, matrix_string):
        self.matrix_list = [[int(number) for number in row.split()]
                            for row in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix_list[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix_list]
