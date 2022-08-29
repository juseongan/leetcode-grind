class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # compute the frequency and sort nums 
        frequency = Counter(nums)
        nums = sorted(list(set(nums)))

        # declare dp array
        maxPoints = [0] * len(nums)
        maxPoints[0] = nums[0] * frequency[nums[0]]
        
        # dp table calculations.
        for idx in range(1, len(nums)):
            points = nums[idx] * frequency[nums[idx]]
            if nums[idx] == nums[idx-1] + 1:
                maxPoints[idx] = max(maxPoints[idx-1], maxPoints[idx-2] + points)
            else:
                maxPoints[idx] = maxPoints[idx-1] + points
                
        return maxPoints[-1]