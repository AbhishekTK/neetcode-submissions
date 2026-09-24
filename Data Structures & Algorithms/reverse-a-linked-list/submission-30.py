# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = d = ListNode()
        p = None
        while head:
            temp = ListNode(head.val,p) 
            # temp.next = p
            head = head.next
            print(temp.val)
            # t = t.next 
            p = temp
            # d = temp
        return p
        