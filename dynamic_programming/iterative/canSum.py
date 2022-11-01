
def canSum(target,n):
    table = [False] * (target+1)
    table[0] = True
    for i in range(target+1):
        if table[i] == True:
            for j in range(len(n)):
                if i + n[j] < len(table):
                    table[i+n[j]] = True
    return table[target]




print(canSum(7,[2,3]))
print(canSum(9,[5,5]))