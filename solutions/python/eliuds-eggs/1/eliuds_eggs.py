def egg_count(display_value):
    
    binary_list = []
    quotient = display_value
    while quotient != 0:
        remainder = quotient % 2
        binary_list.insert(0, remainder)
        quotient = quotient // 2

    return binary_list.count(1)
    