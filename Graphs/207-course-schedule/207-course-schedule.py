class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        
        for x,y in prerequisites:
            graph[x].append(y)
            
        tracked = set()
        visited = set()
        
        def dfs(x):
            if x in tracked: return False
            if x in visited: return False 
            
            tracked.add(x)
            for y in graph[x]:
                if not dfs(y): return False