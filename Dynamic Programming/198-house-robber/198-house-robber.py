class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        if N <= 2:
            return max(nums)
        
        dp = nums
        
        # bottom up approach with dynamic programming
        for i in range(2, N):
            dp[i] = dp[i] + max(nums[:i-1])
        
        return max(dp)