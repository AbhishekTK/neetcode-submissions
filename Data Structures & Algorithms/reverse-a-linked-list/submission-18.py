# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # t = d = ListNode()
        # # t= 
        # p = None
        # while head:
        #     # tt = ListNode()
        #     t = head
        #     t.next = p
        #     head = head.next
        #     p = t
        # return t 
        s = []
        d=r = ListNode()
        while head:
            s.append(head)
            head = head.next
        print(len(s))
        while s:
            t = s.pop()
            r.next = t
            r = r.next
        r.next = None
        return d.next