class Solution:
    # Time Complexity: O(N*2^N)
    # Space Complexity: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k: # if the combination is done
                subsets.append(curr[:])
                return
            
            for i in range(first, len(nums)):
                curr.append(nums[i]) # add nums[i] into the current combination
                
                backtrack(i + 1, curr) # use next integers to complete the combination
                curr.pop()
                
        subsets = []
        for k in range(len(nums) + 1):
            backtrack()
        
        return subsets