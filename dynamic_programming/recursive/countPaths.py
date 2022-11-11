def count_paths(grid):
  cols = len(grid) - 1
  rows = len(grid[0]) - 1
  count = 0
  depth_search(cols,rows,grid,count)
  print(count)
  return count
#Need to track visited
def depth_search(cols,rows,grid,count,visited=set()):
  row_bounds = 0 <= rows < len(grid)
  col_bounds = 0 <= cols < len(grid)
  if not row_bounds or not col_bounds:
    return 
  if grid[cols][rows] == 'X':
    return
  if cols == 0 and rows == 0:
    print("hit")
    count += 1
  if (cols, rows) in visited:
    return
  visited.add((cols,rows))
  depth_search(cols-1,rows,grid,count,visited)
  depth_search(cols+1,rows,grid,count,visited)
  depth_search(cols,rows-1,grid,count,visited)
  depth_search(cols,rows+1,grid,count,visited)
  print(cols,rows)

grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]
count_paths(grid) # -> 5