class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for value in nums: # go through entire array 1 by 1
            if value in numSet: # check if the duplicate exists in the set
                return True
            numSet.add(value)
        return False