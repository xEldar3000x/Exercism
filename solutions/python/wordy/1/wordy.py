def operand_action(a, b, operand):
    result = 0
    match operand:    
        case "+":
            sum_value = a + b
            return sum_value
        case "-":
            sub_value = a - b
            return sub_value
        case "*":
            mult_value = a * b
            return mult_value
        case "/":
            div_value = a / b
            return div_value
    
def answer(question):
    operands = {
    "plus": "+",
    "minus": "-",
    "divided": "/",
    "multiplied": "*"
}
    #Checks for unknown operation in the end of a question
    if question.rstrip("?").split(" ")[-1] in ["cubed", "squared"]:
        raise ValueError("unknown operation")
    
    mathematics = []
    for value in question.rstrip("?").split(" "):
        
        #Checks if there are already a values in a list
        if len(mathematics) >= 1:
            #Checks for two numbers in a row
            if value.isnumeric() and isinstance(mathematics[-1], int):
                raise ValueError("syntax error")
            #Checks for two operators in a row
            if not isinstance(mathematics[-1], int) and value in operands:
                raise ValueError("syntax error")
        try:
            number = int(value)
            mathematics.append(number)
        except ValueError:
            if value in operands:
                mathematics.append(operands[value])
                

    #Checks did the loop find the numbers and operators
    if mathematics == []:
        raise ValueError("syntax error")
    #Checks if the list ends with a value        
    if not isinstance(mathematics[-1], int):
        raise ValueError("syntax error") 
    #Checks if there is only a number
    if len(mathematics) == 1:
        return int(mathematics[0])
        
    result = 0
    for index in range(0, len(mathematics) - 1, 2):
        if index == 0:
            a = mathematics[index]
        else:
            a = result
        
        operand = mathematics[index + 1]
        b = mathematics[index + 2]
        result = operand_action(a, b, operand)
        
    
    
         
    return result
       