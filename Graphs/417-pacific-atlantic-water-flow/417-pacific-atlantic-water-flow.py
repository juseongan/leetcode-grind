# hyochan's sloution 
# dfs
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # Start from all of the perimeter edges
        # Traverse from each perimeter edge
        # There will be 2 groups of perimeter edges: Pacific and Atlantic
        # After traversing from each node in each group, if there
        # are any overlapping nodes, save them to the answer
        
        M, N = len(heights), len(heights[0])
        
        visited = set()
        atlantic = set()
        pacific = set()
        
        # DFS starting from coastal nodes, and only keep on going
        # if the next value is the same or larger
        # Save all the values accessed in sets
        def dfs(y,x,marker):
            if (y,x) in visited: return
            visited.add((y,x))
            
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                ny = y + dy
                nx = x + dx
                
                if ny<0 or nx<0 or ny>=M or nx>=N: continue
                if (ny,nx) in visited: continue
                if heights[ny][nx] < heights[y][x]: continue
                
                if marker=='atlantic': atlantic.add((ny,nx))
                elif marker=='pacific': pacific.add((ny,nx))
                
                dfs(ny,nx,marker)
        
        for i in range(M):
            for j in range(N):
                if i==0 or j==0: pacific.add((i,j))
                if i==M-1 or j==N-1: atlantic.add((i,j))
        
        # Traverse Pacific coastal nodes
        for i in range(M): dfs(i,0,'pacific')
        visited.clear();
        for j in range(N): dfs(0,j,'pacific')
        visited.clear();
        
        # Traverse Atlantic coastal nodes
        for i in range(M): dfs(i,N-1,'atlantic')
        visited.clear();
        for j in range(N): dfs(M-1,j,'atlantic')
        visited.clear();
        
        # Return the intersection of the 2 sets
        return sorted(list(pacific.intersection(atlantic)))
