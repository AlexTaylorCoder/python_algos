
def best_sum(target,a):
    table = [None] * (target+1)
    table[0] = []
    for i in range(target+1):
        #Save in first loop
        if table[i] is not None:
            for j in range(len(a)):
                if a[j]+i < len(table):
                    if table[i+a[j]] is None or len(table[i] + [a[j]]) < len(table[i+a[j]]):
                        table[i+a[j]] = table[i] + [a[j]] 
    return table[-1]

print(best_sum(7,[5,3,4,2,3,1,5]))