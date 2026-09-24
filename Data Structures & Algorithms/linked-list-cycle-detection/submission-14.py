# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s,f = head,head.next

        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s==f:
                return True
        return False