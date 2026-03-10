def commands(binary_str):
    actions ={
        0: "wink",
        1: "double blink",
        2: "close your eyes",
        3: "jump"
    }
    result = []
    for action_number, position_number in enumerate(binary_str[::-1]):
        if position_number == "1":
            try:
                result.append(actions[action_number])
            except KeyError: 
                result.reverse()
                return result
    return result
    