def proverb(*args, **kwargs): 

    if len(args) == 0:

        return list(args)

    kwargs = kwargs.get("qualifier")

    result = []
    
    for first_word, second_word in zip(args, args[1:]):

        result.append(f"For want of a {first_word} the {second_word} was lost.")


    resulting_kwargs = f"{kwargs + " "}" if kwargs else ""

    result.append(f"And all for the want of a {resulting_kwargs}{str(args[0])}.")

    return result