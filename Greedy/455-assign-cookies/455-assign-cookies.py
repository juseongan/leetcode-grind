'''
Precondition: If g[i] is greater than s[i], then g[i+1] must be greater than s[i].

1. Ascend a unsorted lists
2. 현재 주려는 쿠키가 아이가 원하는 쿠키 사이즈보다 크거나 같다면
    아이에게 쿠키를 주고, 다음 아이와 다음 쿠키를 가져옵니다.
3. 현재 주려는 쿠키가 아이가 원하는 쿠키 사이즈보다 작다면
    다음 쿠키를 가져옵니다. (precondition)
4. 쿠키를 받은 아이의 수를 반환합니다.
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # Ascend lists
        g.sort()
        s.sort()
        
        # Declare variable
        '''
        i:  The minimum size of a cookie a child wants
        j:  cookie size
        '''
        i = j = 0
        
        # Find the maximum number of children who received cookies
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
            
        return i
            
'''
Time complexity: O(n)
Space complexity: O(n^2)
'''