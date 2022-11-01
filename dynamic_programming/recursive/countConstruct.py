
def count_construct(target,a, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return 1 
    count = 0
    for ele in a:
        try:
            if target.index(ele) == 0:
                ways = count_construct(target[len(target):],a)
                count += ways
                
        except:
            count = 0
    memo[target] = count
    return count
print(count_construct("purple",["le","purp"]))
print(count_construct("banana",["b","awf"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","ee","eeee","eeeeeeee","eeeeeeeeeeee","eeeeeeeeeeeeeeee"]))

