# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(c,ca):
            if c is None:
                return None
            c.next = rec(c.next,ca)
            ca[0]-=1
            if ca[0]==0:
                return c.next
            return c
        
        return rec(head,[n])