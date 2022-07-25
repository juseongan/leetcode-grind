class Solution:
    # Time Complexity: O(logN)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 # left and right pointers starting at each end
        
        while l <= r:
            pivot = l + (r - l) // 2 # (l + r) // 2 can lead to overflow
            if nums[pivot] == target:
                return pivot
            
            # left sorted portion
            elif nums[pivot] >= nums[l]:
                if nums[l] <= target and target < nums[pivot]: # search left portion
                    r = pivot - 1
                else: # search right portion
                    l = pivot + 1
            
            # right sorted portion
            else:
                if nums[pivot] < target and target <= nums[r]: # search right portion
                    l = pivot + 1
                else: # search left portion
                    r = pivot - 1
        
        return -1