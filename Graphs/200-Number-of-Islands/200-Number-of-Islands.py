# hyebin's solution
# recursive dfs way
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        
        r = len(grid)
        c = len(grid[0])

        def dfs(row,col):
            # Traversal range and condition
            if row < 0 or row >= r \
            or col < 0 or col >= c \
            or grid [row][col] != '1': return # 0 None '' == False
            
            grid[row][col] = 0 # mark visited
            
            # Recursive traversal in north, south, earth and west 
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        # Return the number of island
        island = 0
        for row in range(r):
            for col in range(c):
                if grid[row][col] == '1':
                    dfs(row,col)
                    island+=1
        return island