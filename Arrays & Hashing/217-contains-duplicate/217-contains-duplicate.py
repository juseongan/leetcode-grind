'''
time complexity reference: https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
len(s): O(1) <= because of the 'counter' python has
set(s): O(len()) <= depends on length of iterable, time complexity of worst case is O(n) 
'''
class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)): 
            return False
        else:
            return True