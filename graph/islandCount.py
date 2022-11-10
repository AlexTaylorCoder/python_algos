#Has to go through all possible paths
#In recursive don't check ahead; just put in base case
def island_count(i,j,grid,visited):
  row_bounds = 0 <= i < len(grid)
  col_bounds = 0 <= j < len(grid[0])
  if not row_bounds or not col_bounds:
    return False
  if grid[i][j] == "W":
    return False
  current = (i,j)
  count = 0
  if current in visited:
    return False
  visited.add(current)
  island_count(i+1,j,grid,visited)
  island_count(i-1,j,grid,visited)
  island_count(i,j+1,grid,visited)
  island_count(i,j-1,grid,visited)

  return True

def repeat_count(grid):
    visited = set()
    col = len(grid) 
    row = len(grid[0]) 
    count = 0
    for i in range(col):
        for j in range(row):
          if island_count(i,j,grid,visited):
            count += 1
    return count
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(repeat_count(grid)) # -> 3