class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        # delete
        left.next = left.next.next
        return dummy.next