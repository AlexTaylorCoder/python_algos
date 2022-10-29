
#Keep general structure when bubble up first match
def how_sum(target,a,memo={}):
    if target in memo:
        return memo
    if target == 0:
        return []
    if target < 0:
        return None
    for n in a:
        rem = target - n 
        result = how_sum(rem,a,memo)
        print(result)
        if result is not None:
            memo[target] = result + [n]
            return memo[target]
    memo[target] = None
    return None    


print(how_sum(7,[5,3,4,7]))