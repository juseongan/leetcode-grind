# Two Pointer
'''
Expaln how to slove (Two pointer)
1. 투 포인터를 만든다. 
    from_start: 맨 왼쪽에서 시작하는 포인터
    from_end: 맨 오른쪽에서 시작하는 포인터
2. from_start 포인터가 가리키는 값과 from_end 포인터가 가리키는 값을 swap 한다.
3. from_start 포인터를 한 칸 뒤로, from_end 포인터를 한 칸 앞으로 움직인다.
4. until from_start >= from_end 까지 반복한다.
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # 투 포인터 변수 생성
        from_start, from_end = 0, len(s)-1
        
        # swap
        while from_start < from_end:
            s[from_start], s[from_end] = s[from_end], s[from_start]
            
            # from_start 포인터를 한 칸 뒤로, from_end 포인터를 한 칸 앞으로 움직인다.
            from_start += 1
            from_end -= 1
        return s
'''
Time Complexity: O(n): swap N/2 element.
Space Complexity: O(1)
'''


# pythonic way
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''