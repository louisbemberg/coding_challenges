def solution(coins, quantity):
    # brute force
    # compute all possible combinations of coins and add to set
    from itertools import combinations

    all_coins = []
    for coin, amount in zip(coins, quantity):
        all_coins += [coin]*amount

    sums_set = set([])
    for i in range(len(all_coins)):
        for c in combinations(all_coins, i + 1):
            sums_set.add(sum(c))

    return len(sums_set)
    

def solution(coins, quantity):
    # smarter
    sums_set = {0}
    
    # iterating over each type of coin
    for coin_index, coin in enumerate(coins):
        # copy of current sums_set since it will change during the next iteration
        sums_set_copy = list(sums_set)
        # iterating over previous sums. since our set's first element is 0
        # first loop computes the possible sums of that specific coin.
        # subsequent loops combine those sums with the previous ones.
        for previous_sum in sums_set_copy:
            # possible quantities range from 1 to the actual max amount of coins available
            for j in range(1, quantity[coin_index] + 1):
                # TRICK: recall that previous_sum is 0 for the first iteration,
                #         this allows us to compute the combinations of that specific coin.
                sums_set.add(previous_sum + j * coin)
            
    
    # we added a 0 for the trick, so remove it for final output. 
    return len(sums_set) - 1
    