class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                j = 0
                while num > sub[j]:
                    j += 1
                
                sub[j] = num
                
        return len(sub)