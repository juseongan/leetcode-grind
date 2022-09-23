class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        maxSplit = []
        evenInt = 2
        if finalSum % 2 == 0:
            while evenInt <= finalSum:
                maxSplit.append(evenInt)
                finalSum -= evenInt
                evenInt += 2
            
            maxSplit[-1] += finalSum
        
        return maxSplit