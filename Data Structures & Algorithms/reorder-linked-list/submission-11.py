# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rec(r,c):
            if not c:
                return r
            r = rec(r,c.next)
            if not r:
                return None
            t = None
            if r==c or r.next==c:
                c.next=None
            else:
                t = r.next
                r.next = c
                c.next = t
            return t
        head = rec(head,head.next)