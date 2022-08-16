class Solution:
    # Author: juseongan
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        charFreq = {}
        for i in s:
            if i in charFreq:
                charFreq[i] += 1
            else:
                charFreq[i] = 1
        
        # find the index
        for idx, ch in enumerate(s):
            if charFreq[ch] == 1:
                return idx   
        
        return -1