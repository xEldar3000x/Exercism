def sum_of_multiples(limit, multiples):
    result = set()
    for base_number in multiples:
        if base_number == 0:
            continue
        result.update(range(base_number, limit, base_number))
        
    return sum(result)
