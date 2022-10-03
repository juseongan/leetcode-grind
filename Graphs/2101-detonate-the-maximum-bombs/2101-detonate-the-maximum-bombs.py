class Solution:
    # DFS Approach
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(i):
            dq, maxBombs = [i], [i]
            while len(dq) > 0:
                i = dq.pop()
                for j in adj[i]:
                    if j not in maxBombs and j not in dq:
                        dq.append(j)
                        maxBombs.append(j)
            return len(maxBombs)

        # construct the adjacency matrix of the directed graph
        adj = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                    adj[i].append(j)
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[j][2] ** 2:
                    adj[j].append(i)
        
        maxBombs = 0
        # traverse each bomb as the starting point and count the number of nodes it can reach on graph.
        for i in range(len(bombs)):
            maxBombs = max(maxBombs, dfs(i))
        return maxBombs