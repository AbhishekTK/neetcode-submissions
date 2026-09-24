# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # p, c = None,head
        # while c:
        #     t = c.next
        #     c.next = p
        #     p = c
        #     c = t
        # return p
        if head == None:
            return None
        
        nh = head
        if head.next:
            nh = self.reverseList(head.next)
            head.next.next = head 
        head.next = None
        return nh
