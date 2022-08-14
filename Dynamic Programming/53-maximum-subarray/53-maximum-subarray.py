'''
sliding window concept

If prefix sum is negative, remove the result current sum.
If current value is negative, It's ok because we store every maximum sum.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = num[0]
        max_subarray = 0
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += num
            max_subarray = max(max_subarray, current_sum)
            
        return max_subarray
'''
Time complexity: O(n)
Space complexity: O(n)
'''