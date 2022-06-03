class Solution:
    # Time Complexity: O(N^(T/M+1))
    # Space Complexity: O(T/M)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, curr, start):
            if remain == 0:
                # make a deep copy of the current combination
                combination.append(list(curr))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                curr.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], curr, i)
                # backtrack, remove the number from the combination
                curr.pop()
                
        combination = []
        backtrack(target, [], 0)
        
        return combination