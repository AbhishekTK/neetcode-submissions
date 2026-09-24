# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = head
        l = []
        while c:
            l.append(c)
            c= c.next
        
        ri= len(l)-n
        if ri==0:
            return head.next
        l[ri-1].next= l[ri].next
        return head 
