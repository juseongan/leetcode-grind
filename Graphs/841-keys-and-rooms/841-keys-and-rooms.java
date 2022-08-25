import java.util.List;
import java.util.Stack;

class Solution {
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        visited[0] = true;
        Stack<Integer> keyStack = new Stack();
        keyStack.push(0);

        while (!keyStack.isEmpty()) {
            int key = keyStack.pop();
            for (int room: rooms.get(key))
                if (!visited[room]) {
                    visited[room] = true;
                    keyStack.push(room);
                }
        }

        for (boolean v: visited)
            if (!v) return false;
        return true;
    }
}