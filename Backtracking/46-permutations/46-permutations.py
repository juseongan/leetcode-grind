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