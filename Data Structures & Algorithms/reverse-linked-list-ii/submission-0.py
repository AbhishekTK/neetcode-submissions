# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d = ListNode(0,head)
        lp,c = d,head
        for _ in range(left-1):
            lp,c = c,c.next
        p = None
        for _ in range(right-left+1):
            t = c.next
            c.next = p
            p,c= c,t
        
        lp.next.next = c
        lp.next = p
        return d.next