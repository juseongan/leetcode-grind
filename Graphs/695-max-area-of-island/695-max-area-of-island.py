class Solution:
    # Time Complexity: O(rows * cols)
    # Space Complexity: O(rows * cols)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            # out of bound
            if r < 0 or r == rows or c < 0 or c == cols:
                return 0
            # empty
            elif grid[r][c] == 0:
                return 0
            # visited
            elif (r, c) in visited:
                return 0
            
            visited.add((r, c))
            return (1 + dfs(r + 1, c)
                      + dfs(r - 1, c)
                      + dfs(r, c + 1)
                      + dfs(r, c - 1))
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(dfs(r, c), maxArea)
        
        return maxArea