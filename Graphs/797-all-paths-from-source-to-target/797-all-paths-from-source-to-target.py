class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        N = len(graph)
        paths = []
        
        def dfs(here, path):
            if here == N-1:
                paths.append(path)
                print(path)
            
            for there in graph[here]:
                dfs(there, path + [there])
        
        dfs(0, [0])
        
        return paths