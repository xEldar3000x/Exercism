def gamestate(board):
    board_string = "".join(board)
    #Checks if O started the game
    if board_string.count("O") > board_string.count("X"):
        raise ValueError("Wrong turn order: O started")
    #Checks if X went twice
    if board_string.count("O") == 0 and board_string.count("X") == 2:
        raise ValueError("Wrong turn order: X went twice")
    #Checks if X and O won    
    if "OOO" in board and "XXX" in board:
        raise ValueError("Impossible board: game should have ended after the game was won")

    #Converts a list of strings to a list of lists
    listed_values = []
    for row in board:
        listed_values.append(list(row))

    win = 0
    #Looks for a horizontal solution
    for y_coordinate in [0, 1, 2]:
        row_values = []
        for x_coordinate in [0, 1, 2]:
            current_cell = listed_values[y_coordinate][x_coordinate]
            row_values.append(current_cell)    
            if (row_values.count("O") or row_values.count("X"))  == 3:
                win += 1
                
    #Looks for a vertical solution           
    for x_coordinate in [0, 1, 2]:
        column_values = []
        for y_coordinate in [0, 1, 2]:
            current_cell = listed_values[y_coordinate][x_coordinate]           
            column_values.append(current_cell)  
            if (column_values.count("O") or column_values.count("X"))  == 3:
                win += 1
    #Checks if they won by row and column simultaneously           
    if win == 2:
        return "win"
        
    #Looks for a left diagonal solution
    diagonal_values = []
    for coordinate in [0, 1, 2]:
        current_cell = listed_values[coordinate][coordinate]
        diagonal_values.append(current_cell)
        if (diagonal_values.count("O") or diagonal_values.count("X")) == 3:
                win += 1
            
    #Looks for a right diagonal solution
    diagonal_values = []
    for coordinate in [0, 1, 2]:
        current_cell = listed_values[coordinate][2 - coordinate]
        diagonal_values.append(current_cell)
        if (diagonal_values.count("O") or diagonal_values.count("X")) == 3:
                win += 1
            
    #Checks if they won by 2 diagonals simultaneously 
    if win == 2:
        return "win"        
    elif win == 1:
        return "win"
        
            
    #If didnt win, then a draw or ongoing             
    if " " not in board_string:
        return "draw"

    return "ongoing"
