# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = c = head
        co=0
        while c:
            c = c.next
            co+=1
        if co==1:
            print("early return []")
            return None
        print(co)
        c = head
        if co-n==0:
            return c.next
        while co-n-2>=0:
            print(co,n,co-n,c.val)
            co-=1
            c = c.next
        print(c.val)
        c.next = c.next.next
        return d