#Can use breadth first and hold distance in visited
def grid_check(grid):
    col = len(grid)
    row = len(grid[0])
    visited = set()
    min = 999999999
    for i in range(col):
        for j in range(row):
            #Depth first count
            path_count = depth_count(i,j,grid,visited)
            print(path_count)
            if path_count:
                if path_count < min:
                    min = path_count
    return min

def depth_count(col,row,grid,visited):
    col_bounds = 0 <= col < len(grid)
    row_bounds = 0 <= row < len(grid[0])

    if not col_bounds or not row_bounds:
        return False
    pos = (row,col)
    if grid[col][row] == 'W':
        return False
    if pos in visited:
        return False
    visited.add(pos)
    count = 1
    count += depth_count(col+1,row,grid,visited)
    count += depth_count(col-1,row,grid,visited)
    count += depth_count(col,row+1,grid,visited)
    count += depth_count(col,row-1,grid,visited)
    return count
    



grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]


print(grid_check(grid)) # -> 2