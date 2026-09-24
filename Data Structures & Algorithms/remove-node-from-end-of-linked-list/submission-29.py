# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        def rec(c,tc):
            if c == None:
                print("base")
                return 0
            print(c.val,tc)
                # rec(c.next,n+1)
            # if tc == n:
                # return head.next
            rc = rec(c.next,tc+1)
            print(rc)
            if rc == n:
                if c.next or c.next.next:

                    c.next = c.next.next
                else:
                    c.next=None
            return rc+1
            
        if (rec(head,1)) == n:
            return head.next
        return head
