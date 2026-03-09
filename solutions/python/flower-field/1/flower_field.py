def annotate(garden):
    #In coding there is always a test with an empty input, so i will speedrun it
    if garden == []:
        return []
    
    rows_values = []
    flower_indexes = []
    for row_index, row in enumerate(garden):
        rows_values.append(list(row))
        for value_index, value in enumerate(row):
            if value == "*":
                flower_indexes.append([row_index, value_index])
            elif value == " ":
                continue
            else: 
                raise ValueError("The board is invalid with current input.")
            
    #Checks for different sizes of a rows/columns
    control_len = len(rows_values[0])
    for row in rows_values:
        if len(row) != control_len:
            raise ValueError("The board is invalid with current input.")

    for flower_index in flower_indexes:
        for cell_x in [-1, 0, 1]:
            for cell_y in [-1, 0, 1]:
                if cell_x == 0 and cell_y == 0:
                    continue
                #Case for a singular horizontal matrix
                try:
                    value_x = flower_index[1] + cell_x
                except IndexError:
                    value_x = 0
                try:
                    value_y = flower_index[0] + cell_y
                except IndexError: 
                    value_y = 0

                #Makes sure so we won't analyze cells out of matrix
                if 0 <= value_x < len(rows_values[0]) and 0 <= value_y < len(rows_values):
                    if rows_values[value_y][value_x] == "*":
                        continue
                    if isinstance(rows_values[value_y][value_x], int):
                        rows_values[value_y][value_x] += 1
                    else:
                        rows_values[value_y][value_x] = 1
                        

    for row in rows_values:
        string_row =""
        for value in row:
            string_row += str(value) 
        rows_values[rows_values.index(row)] = string_row
            
    return rows_values
