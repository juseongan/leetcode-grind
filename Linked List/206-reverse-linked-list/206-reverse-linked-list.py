# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr: # reverse the pointers
            temp = curr.next
            
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev