# hyebin's solution
class Solution:
    '''
    nums is array of distinct integers, 1 <= nums.length <= 6
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def dfs(elements, pre_elements = []):
            if len(elements) == 0: permutations.append(pre_elements[:])
                
            for element in elements:
                next_elements = elements[:]
                next_elements.remove(element)
                
                pre_elements.append(element)
                dfs(next_elements)
                pre_elements.pop()
                
        dfs(nums)
        return permutations

# hyebin's solution
class Solution:
    '''
    if nums = [1,2,3]    -> len(nums) == n
                []        -> permutation 
               / | \ 
            [1] [2] [3]   -> choose one in nums: n cases
            /\   /\  /\       
        [2,3]             -> choose one in nums (except num choosen): (n-1) cases
        /   
    [1,2,3]               -> choose one in nums (except num choosen): 1 case

    Finally, we must have to merge each permutation
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = []
        
        def dfs(nums):
            if len(nums) == 0: 
                permutations.append(permutation[:])
                
            for num in nums:
                new_nums = nums[:]
                new_nums.remove(num)
                
                permutation.append(num)
                dfs(new_nums)
                permutation.pop()
                
        dfs(nums)
        return permutations