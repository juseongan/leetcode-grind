class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return [] # edge case

        pCount, sCount = [0] * 26, [0] * 26
        # build reference array using string p
        for i in p:
            pCount[ord(i) - ord('a')] += 1
        
        output = []
        # sliding window on the string s
        for r in range(len(s)):
            # add one more letter 
            # on the right side of the window
            sCount[ord(s[r]) - ord('a')] += 1
            # remove one letter 
            # from the left side of the window
            if r >= len(p):
                sCount[ord(s[r - len(p)]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if pCount == sCount:
                output.append(r - len(p) + 1)
        
        return output