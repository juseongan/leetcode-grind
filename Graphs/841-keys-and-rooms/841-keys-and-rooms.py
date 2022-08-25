class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        
        keyStack = [0]
        while keyStack:
            key = keyStack.pop()
            
            for room in rooms[key]:
                if not visited[room]:
                    visited[room] = True
                    keyStack.append(room)
        return all(visited)