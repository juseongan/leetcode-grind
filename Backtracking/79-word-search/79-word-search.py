class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        
        def backtrack(row, col, idx):
            # base case: we find match for each letter in the word
            if idx == len(word):
                return True
            # check the current status, before jumping into backtracking
            if (
                row < 0 or row == rows or
                col < 0 or col == cols or
                board[row][col] != word[idx] or
                (row, col) in path
            ):
                return False

            # mark the choice before exploring further.
            path.add((row, col))
            
            # explore the 4 neighbor directions
            result = False
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                result = backtrack(row+rowOffset, col+colOffset, idx+1)
                if result:
                    break # break instead of return directly to do some cleanup afterwards
            
            # revert the change, a clean slate
            path.remove((row, col))
            # tried all directions, and did not find any match
            return result
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        
        # no match found after all exploration
        return False