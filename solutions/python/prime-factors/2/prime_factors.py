def factors(value):
    result = []
    while value % 2 == 0:
        result.append(2)
        value = value // 2
        
    odd_number = 3
    while value != 1:
        if value % odd_number == 0:
            result.append(odd_number)
            value = value // odd_number
        else:
            odd_number = odd_number + 2
    return result
    