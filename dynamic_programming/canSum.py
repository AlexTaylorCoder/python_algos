
def canSum(target, a, memo={}):
    if target < 0:
        return False
    if target == 0:
        return True 
    if target in memo:
        return memo[target]

    for n in a:
        rem = target - n
        memo[rem] = canSum(rem,a,memo)
        if memo[rem]:
            return True
    return False


print(canSum(8,[2,3,5]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(300,[7,14]))