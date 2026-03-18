def find_fewest_coins(coins, target):
    #The BFS algorithm was used, which accumulates all possible sums layer by layer
    if target == 0:
        return []
    
    if target < 0:
        raise ValueError("target can't be negative")

    if min(coins) > target:
        raise ValueError("can't make target with given coins")

    #The BFS algorithm
    found_sums = [0]
    found_sum_combinations = {}
    visited = {0}
    while found_sums:
        current_sum = found_sums.pop(0)
        
        for coin in coins:
            new_sum = coin + current_sum
            
            if new_sum > target or new_sum in found_sums:
                continue

            found_sums.append(new_sum)
            visited.add(new_sum)
            
            if new_sum not in found_sum_combinations:
                found_sum_combinations[new_sum] = (current_sum, coin)
            
            #When target is found it goes reverse in dictionary
            if new_sum == target:
                result = []
                while target != 0:
                    current_sum, coin = found_sum_combinations[target]
                    result.append(coin)
                    target -= coin
    
                return sorted(result)
    raise ValueError("can't make target with given coins")