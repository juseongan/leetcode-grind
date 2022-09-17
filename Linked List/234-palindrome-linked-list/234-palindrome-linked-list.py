'''
hyebin's solution
Way1. convert linked list to list 
'''
# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        queue = []
        
        # convert linked list to list
        while node is not None: # check empty List
            queue.append(node.val)
            node = node.next
        
        # check palindrome
        '''
        same as 'return queue == queue[::-1]'
        '''
        while len(queue) > 1:               
            if queue.pop(0) != queue.pop(): 
                return False
        return True
'''
time complexity: O(n^2)
space complexity: O(n) 'queue'
'''

# way2. deque (faster than above)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = collections.deque()
        
        # check empty list
        if not head: 
            return True
        
        node = head
        while node is not None:
            queue.append(node.val)
            node = node.next            
            
        while len(queue)>1:
            if queue.popleft() != queue.pop():
                return False
        return True
'''
time complexity: O(n)
space complexity: O(n)
'''
