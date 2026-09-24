# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        nh = head
        if head.next:
            head = self.reverseList(head.next)
            nh.next.next = nh
        nh.next = None
        return head