    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]: # skip duplicate nums
                continue
            
            l, r = index+1, len(nums)-1 # implementation of 167-two-sum-II
            while l < r: # go through the string before the pointers meet or cross each other
                numSum = value + nums[l] + nums[r]  # compute the sum of current value and pointed numbers

                if numSum == 0: # move the pointers until the end
                    result.append([value + nums[l] + nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif numSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return result