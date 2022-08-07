class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # num  > 0 -> ignore
        # num == 0 -> ruins all
        # num  < 0 -> has to have even # of negative values 
        
        N = len(nums)
        sequences, temp = [], ""
        
        for num in nums:
            if num == 0:
                sequences.append(temp)
                temp = ""
            else:
                temp += "+" if num > 0 else "-" 
                    
        if len(temp) > 0:
            sequences.append(temp)
        
        answer = 0
        for seq in sequences:
            if seq.count("-") % 2 == 0:
                answer = max(answer, len(seq))
            else:
                remove_left_minus = len( seq[seq.find("-")+1:] )
                remove_right_minus = len( seq[:seq.rfind("-")])
                answer = max(answer, max(remove_left_minus, remove_right_minus))
        return answer