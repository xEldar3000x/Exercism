def convert(input_grid):
    #Checks if number of input lines multiple of four
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    ocr_dictionary = {
    (" _ ", "| |", "|_|"): "0",
    ("   ", "  |", "  |"): "1",
    (" _ ", " _|", "|_ "): "2",
    (" _ ", " _|", " _|"): "3",
    ("   ", "|_|", "  |"): "4",
    (" _ ", "|_ ", " _|"): "5",
    (" _ ", "|_ ", "|_|"): "6",
    (" _ ", "  |", "  |"): "7",
    (" _ ", "|_|", "|_|"): "8",
    (" _ ", "|_|", " _|"): "9",
}
    
    #Rearranges the column input into inline input 1\n2\n3 -> 1,2,3
    if len(input_grid[0]) < len(input_grid) and len(input_grid) > 4:
        #Collects original size for commas placement in the end
        input_length = len(input_grid)
        input_height = len(input_grid[0])
        
        rearranged_input_grid = []
        row_number = -1
        for row in input_grid:
            row_number +=1
            if row_number == 4:
                break
            rearranged_input_grid.append(row)
            for index in range(1, len(input_grid) // 4):
                rearranged_input_grid[row_number] += input_grid[row_number + 4 * index]
        input_grid = rearranged_input_grid    
    listed_numbers = []
    #Converts to a list of rows
    for row in input_grid:
        #Checks if the number of input columns is not a multiple of three
        if len(row) % 3:
           raise ValueError("Number of input columns is not a multiple of three") 
        listed_numbers.append(list(row))
        
    #Collects the values from a cell 3x3, identifies the number and then moves left to the next 3x3 cell    
    result = ""
    line_of_a_number = ""
    key = []
    for position_of_a_number in range(0, len(listed_numbers[0]) + 1, 3):
        try:
            result += ocr_dictionary[tuple(key)]
        except KeyError:
            result += "?"
        finally: 
            key = []
            number = []
            line_of_a_number = ""
        if position_of_a_number == len(listed_numbers[0]):
            break
        for y_coordinate in range(len(listed_numbers)):
            if y_coordinate > 0:
                key.append(line_of_a_number)
                line_of_a_number = ""
            for x_coordinate in range(3):
                current_cell = listed_numbers[y_coordinate][x_coordinate + position_of_a_number]
                line_of_a_number += current_cell
    try:
        comma_result = list(result)
        for comma_index in range(0, len(result) - input_length // 3, input_length // 3):
            comma_result.insert(comma_index + input_length // 3, ",")
        result = "".join(comma_result)
        return result[1:]
    except UnboundLocalError:                  
        return result[1:]