#Similar to howSum, return array with shortest length

def bestSum(target,a, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    
    shortest = None
    for n in a:
        valid_sum = bestSum(target-n,a, memo)
        if valid_sum is not None:
            combo = valid_sum + [n]
            if (shortest == None or len(shortest) > len(combo)):
                shortest = combo
    memo[target] = shortest
    return shortest

print(bestSum(8,[2,3,5]))
print(bestSum(7,[5,3,4,7]))
print(bestSum(7,[2,4]))
print(bestSum(300,[7,14]))
