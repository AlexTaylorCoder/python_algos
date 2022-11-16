#https://leetcode.com/problems/number-of-islands/?envType=study-plan&id=level-1

    def numIslands(self, grid):
        # Iterate through each, if land dfs
        # If not in visited then add
        # Instead of keeping visited array can just turn each visited element to 0
        def check_item(grid):
            cols = len(grid) - 1
            rows = len(grid[0]) - 1
            visited = set()
            count = 0
            for c in range(cols+1):
                for r in range(rows+1):
                    isIsland = dfs(grid,c,r,visited)
                    if isIsland:
                        count += isIsland
            return count
        def dfs(grid,c,r,visited):
            col_bounds = 0 <= c < len(grid) 
            row_bounds = 0 <= r < len(grid[0])

            if not col_bounds or not row_bounds:
                return False
            if grid[c][r] == "0":
                return False
            pos = (c,r)
            if pos in visited:
                return False
            visited.add(pos)
            dfs(grid,c+1,r,visited)
            dfs(grid,c-1,r,visited)
            dfs(grid,c,r+1,visited)
            dfs(grid,c,r-1,visited)
            return True
        return check_item(grid)

print(numIslands(grid))
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]