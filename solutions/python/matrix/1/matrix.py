class Matrix:
    def __init__(self, matrix_string):
        matrix_string = matrix_string + " "
        position = 0
        start = 0
        end = 0
        self.matrix_list = [[]]
        for char in matrix_string:
            
            if char == " ":
                number = int(matrix_string[start:end])
                self.matrix_list[position].append(number)
                start = end + 1
                end += 1
                continue
                
            if char == "\n":
                number = int(matrix_string[start:end])
                self.matrix_list[position].append(number)
                self.matrix_list.append([])
                position += 1
                start += 1
            end +=1

    def row(self, index):
        return self.matrix_list[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix_list]
