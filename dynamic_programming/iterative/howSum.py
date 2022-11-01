
def how_sum(target,a):
    table = [None] * (target+1)
    table[0] = []
    for i in range(target+1):
        if table[i] is not None:
            for j in range(len(a)):
                if i + a[j] < len(table):
                    table[i+a[j]] = table[i] + [a[j]]

    return table[-1]

print(how_sum(7,[5,3,4,2,3,1,5]))