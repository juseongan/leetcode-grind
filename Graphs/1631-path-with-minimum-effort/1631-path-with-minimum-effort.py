from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        M, N = len(heights), len(heights[0])
        
        path_max_effort = [[float('inf') for _ in range(N)] for _ in range(M)]
        
        def dijkstras(i, j):
            queue = deque([])
            queue.append((i,j))
            path_max_effort[i][j] = 0
            
            while queue:
                y, x = queue.popleft()
                
                for dy, dx in [[1,0], [0,1], [-1,0], [0,-1]]:
                    ny, nx = y+dy, x+dx
                    
                    if ny<0 or nx<0 or ny>=M or nx>=N:
                        continue
                    
                    effort_now = abs(heights[ny][nx] - heights[y][x])
                    
                    if max(path_max_effort[y][x], effort_now) < path_max_effort[ny][nx]:
                        path_max_effort[ny][nx] = max(path_max_effort[y][x], effort_now)
                        queue.append((ny,nx))
            
        dijkstras(0, 0)
        
        return path_max_effort[M-1][N-1]