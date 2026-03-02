def proverb(*input, **qualifier): 

    if len(input) == 0:

        return list(input)

    qualifier = qualifier.get("qualifier")

    result = []

    #if len(input) == 1:

        #return [f"And all for the want of a {str(input[0])}."]
    
    for first_word, second_word in zip(input, input[1:]):

        result.append(f"For want of a {first_word} the {second_word} was lost.")


    resulting_qualifier = f"{qualifier + " "}" if qualifier != None else ""

    result.append(f"And all for the want of a {resulting_qualifier}{str(input[0])}.")

    return result


