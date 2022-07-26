class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum,index,sum_path):
            if sum < 0:
                return 
            
            if csum == 0:
                result.append(sum_path)
                return 
            
            for i in range(index,len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
                
        dfs(target, 0, [])
        return result