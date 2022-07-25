class Solution:
    # Time Complexity: O(logN)
    # Space Complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        l, r = 0, len(nums)-1 # left and right pointers starting at each end
        
        while l <= r:
            # portion is sorted
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break
            
            # the portion is not sorted
            pivot = l + (r - l) // 2 # (l + r) // 2 can lead to overflow
            
            minVal = min(minVal, nums[pivot])
            
            if nums[pivot] >= nums[l]: # pivot is in the left sorted portion
                l = pivot + 1 # search the right portion
            else:
                r = pivot - 1 # search the left portion
        
        return minVal