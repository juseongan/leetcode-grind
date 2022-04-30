class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 # left and right pointers starting at each end
        
        while l < r: # go through the string before the pointers meet or cross each other
            numSum = numbers[l] + numbers[r]  # compute the sum of pointed numbers
            
            if numSum == target: # move the pointers until target is met
                return [l+1, r+1]
            elif numSum < target:
                l += 1
            else:
                r -= 1