class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # value:index
        for index, value in enumerate(nums): # go through entire array 1 by 1
            diff = target - value 
            if diff in numMap: # check if the difference exists in the map
                return [numMap[diff], index]
            numMap[value] = index