class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {} # char:frequency
        record = 0
        
        maxFreq = 0
        left = 0
        for right in range(len(s)):
            charMap[s[right]] = charMap.get(s[right], 0) + 1
            
            maxFreq = max(maxFreq, charMap[s[right]]) # this trick increases time efficiency
            
            # slide the left edge if necessary replacement exceeds k
            # while (right - left + 1) - max(charMap.values()) > k: # window length - max frequency
            while (right - left + 1) - maxFreq > k:
                charMap[s[left]] -= 1
                left += 1
            
            record = max(record, right - left + 1)
            
        return record