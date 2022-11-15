def max_path_sum(grid):
  col = len(grid) - 1
  row = len(grid[0]) - 1
  return max_path_recurse(col,row,grid)

def max_path_recurse(col,row,grid):
  col_bounds = 0 <= col < len(grid)
  row_bounds = 0 <= row < len(grid[0])
  if not col_bounds or not row_bounds:
    return 0 
  if col == 0 and row == 0:
    return grid[col][row]
  count = max_path_recurse(col-1,row,grid) + max_path_recurse(col,row-1,grid)
  print(count)
  return count


grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
print(max_path_sum(grid))# -> 18