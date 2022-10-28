
def grid_traveler(n,m, memo={}):
    if (n,m) in memo:
        return memo[(n,m)]
    if (m,n) in memo:
        return memo[(m,n)]
    if n == 1 or m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    
    memo[(n,m)] = grid_traveler(n-1,m,memo) + grid_traveler(n,m-1,memo)
    return memo[(n,m)]



print(grid_traveler(18,34))