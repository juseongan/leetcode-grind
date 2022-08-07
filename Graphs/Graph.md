# Graphs

## Index
1. Problems
2. [Solution Type]
3. [Summarize](#summarize)

<br>

## Problems
* 1-two-sum [(click)](https://leetcode.com/problems/reconstruct-itinerary/) (Solution [click](../내부.py)) (Extra Explanation [click])
* 36-valid-sudoku [()]() (Solution [[click]](../내부.py)) 

<br> 

## Solution Type
### DFS
* Pseudocode
    * using recursive

            DFS(G, v)
                label v as discovered
                for all directed edges from v to w that are in G.adjacentEdges(v) do
                    if vertex w is not labeled as discovered then
                        recursively call DFS(G, W)
        <br>

        * python represent for Pseudocode

        ~~~python
        def recursive_def(v, discovered=[]):
            discovered.append(v)
            for w in graph[v]:
                if not w in discovered:
                    discovered = recursive_dfs(w, discovered)
            return discovered
        ~~~

    * using stack

          DFS-iterative(G, v)
            let S be a stack
            S.push(v)
            while S is not empty do
                v = S.pop()
                if v is not labeled as discovered then
                    label v as discovered
                    for all edges from v to w in G.adjacentEdges(v) do
                        S.push(w)  

        <br>

        * python represent for Pseudocode

        ~~~python
        def iterative_dfs(start_v):
            discovered = []
            stack = [start_v]
            while stack:
                v = stack.pop()
                if v not in discovered:
                    discovered.append(v)
                    for w in graph[v]:
                        stack.append(w)
            return discovered
        ~~~

* Time Complexity
    * Big-O O(|V|)+|E|)
    * 

    <br>

### BFS
* Pseudocode

<br>

* Time Complexity
    * Big-O O(|V|)+|E|)

<br>

### Topological Sort
* Pseudocode

<br>

* Time Complexity
    * Big-O O(|V|)+|E|)

<br>
