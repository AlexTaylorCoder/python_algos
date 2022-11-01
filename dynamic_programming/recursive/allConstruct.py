
def all_construct(target,a,memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return [[]]
    result = []
    for ele in a:
        try:
            if target.index(ele) == 0:
                suffixWays = all_construct(target[len(ele):],a)
                targetWays = list(map(lambda x: x + [ele] ,suffixWays))
                result.append(*targetWays)
        except:
            pass
    memo[target] = result
    return result


print(all_construct("purple",["le","purp","pur","p"]))
print(all_construct("banana",["ba","a","na"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","ee","eeee","eeeeeeee","eeeeeeeeeeee","eeeeeeeeeeeeeeee"]))