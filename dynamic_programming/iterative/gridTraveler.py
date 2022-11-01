

def grid_traveler(r,c):
    arr = [[0]*(c+1) for _ in range(r+1)]
    arr[1][1] = 1
    for i in range(r+1):
        # Range is exclusive so must add 1
        for j in range(c+1):
            current = arr[i][j]
            if j < c:
                arr[i][j+1] += current
            if i < r:
                arr[i+1][j] += current
    return arr[r][c]


print(grid_traveler(3,3))