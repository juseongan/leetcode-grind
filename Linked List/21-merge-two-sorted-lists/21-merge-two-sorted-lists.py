# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # maintain an unchanging reference to node ahead of the return node
        prehead = ListNode()
        
        prev = prehead
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            
            else:
                prev.next = list2
                list2 = list2.next
            
            prev = prev.next
            
        # connect the remainder of l1 or l2
        if list1:
            prev.next = list1
        elif list2:
            prev.next = list2
        
        return prehead.next