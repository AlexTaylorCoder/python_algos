
# Brute force
# Memoize
# base cases
# Check if any elements of array can fit in target
# Subtract target - element
# if element is " " return true
def canConstruct(target,a,memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return True
    for ele in a:
        if target.index(ele) == 0:
            if canConstruct(target[len(target):],a) is True:
                memo[target] = True
                return True
        memo[target] = False
        return False


print(canConstruct("abc",["ab","abc","cd","def","abcd"]))