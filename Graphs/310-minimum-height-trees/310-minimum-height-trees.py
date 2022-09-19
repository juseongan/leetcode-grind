# hyebin's solution
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        n is nodes labelled from 0 to n-1
        edges: the number of edge is n-1
        '''
        if n <= 1:
            return [0]
        
        graph = collections.defaultdict(list)
        
        # represent un-directed tree as 'bi-directed graph'
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # fine leaf node (==leaf node has only one adjacent node)
        leaves = []
        for node_number in range(n+1):         # node number is 0 to n-1 -> repeat n times
            if len(graph[node_number]) == 1:
                leaves .append(node_number)

        # remove leaf node and find leaf node in removed tree           
        while n > 2:
            # remove leaf node                    
            leaves_new = []
            for cur_leaf in leaves:                
                adj_node = graph[cur_leaf].pop()      
                graph[adj_node].remove(cur_leaf)

                # find new leaf node    
                if len(graph[adj_node]) == 1:
                    leaves_new.append(adj_node)

            n -= len(leaves)    
            leaves = leaves_new
            
        return leaves