import math
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
        
    '''The upper bound which is higher and near to the nth prime number'''
    limit = int(number * math.log(number) + 10) * 2
    sieve = [True] * limit
    sieve[0] = False
    sieve[1] = False
    
    nth_prime = 1
    count = -1
    for value in sieve:
        count += 1  
        if value == True and nth_prime == number:
            return count
        elif value == False:
            continue
            
        for multiple in range(count ** 2, limit, count):
            sieve[multiple] = False
        
        nth_prime += 1
        
    return count