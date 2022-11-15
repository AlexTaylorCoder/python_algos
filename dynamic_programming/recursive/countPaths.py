def count_paths(grid):
  cols = len(grid) - 1
  rows = len(grid[0]) - 1
  return depth_search(cols,rows,grid)
#Need to track visited
def depth_search(cols,rows,grid):
  row_bounds = 0 <= rows < len(grid[0])
  col_bounds = 0 <= cols < len(grid)
  print(col_bounds,row_bounds)
  if not row_bounds or not col_bounds:
    return 0
  if grid[cols][rows] == 'X':
    return 0
  if cols == 0 and rows == 0:
    return 1
  count = depth_search(cols-1,rows,grid) + depth_search(cols,rows-1,grid)
  return count
  
  
grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
  ["X", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O"],
]
print(count_paths(grid)) # -> 42