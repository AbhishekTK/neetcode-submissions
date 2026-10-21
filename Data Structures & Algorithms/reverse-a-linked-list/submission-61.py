# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = d = head
        p = None
        while head:
            t = head.next
            head.next = p
            p = head
            head = t
            # t = t.next
        return d