# iteractive (stack) -> Wrong

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph) - 1 
        path = [] 
        visited = []
        
        def dfs(source, target, visited):
            visited.append(source)
            if source == target:
                path.append(visited.copy())
                
            for adjacent_vertex in graph[source]:
                dfs(adjacent_vertex, target, visited)
                
            visited.pop()
            return path
        
        return dfs(0, target, visited)