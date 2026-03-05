def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    ten_base_number = 0
    for index, value in enumerate(digits):
        if value >= 0 and value < input_base:
            ten_base_number += value * input_base ** (len(digits) - index -1)
            
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        
    if ten_base_number == 0:
        return [0]

    if output_base == 10:
        return list(map(int, str(ten_base_number)))

        
    remainder = []
    while ten_base_number > 0:
        remainder.insert(0, ten_base_number % output_base)
        ten_base_number //= output_base

    return remainder
        
        