# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = []

        # head is node
        while head is not None:
            queue.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if queue.pop(0) != queue.pop():
                return False
        
        return True