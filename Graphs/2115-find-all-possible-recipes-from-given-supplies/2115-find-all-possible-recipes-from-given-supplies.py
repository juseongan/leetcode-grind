from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        visited = set()
        graph = {}
        indegree = {}
        
        for idx, recipe in enumerate(recipes):
            
            for ingredient in ingredients[idx]:
                if ingredient not in graph:
                    graph[ingredient] = [recipe]
                else:
                    graph[ingredient] += [recipe]
                
                if ingredient not in indegree:
                    indegree[ingredient] = 0
                if recipe in indegree:
                    indegree[recipe] += 1
                else:
                    indegree[recipe] = 1
        
        queue = deque([])        
        for food, indegree_val in indegree.items():
            if indegree_val == 0 and food in supplies:
                queue.append(food)
        
        def dfs(here):
            if indegree[here] > 0:
                return
            print(here)
            if here not in visited:     
                visited.add(here)
            if here in graph:
                for there in graph[here]:
                    indegree[there] -= 1
                    dfs(there)
        
        while queue:
            food = queue.popleft()
            visited.add(food)
            dfs(food)
        
        print(indegree)
        
        return [recipe for recipe in recipes if recipe in visited]