class Solution:
    # Time Complexity: O(logN)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 # left and right pointers starting at each end
        
        while l <= r:
            pivot = l + (r - l) // 2 # (l + r) // 2 can lead to overflow
            if nums[pivot] < target:
                l = pivot + 1
            elif nums[pivot] > target:
                r = pivot - 1
            else:
                return pivot
        
        return -1