# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # s = []
        d = t = ListNode(0,head)
        # d = head
        groupPrev = d
        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next
            while curr!=groupNext:
                tmp = curr.next  
                curr.next = prev
                prev =  curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return d.next

    def getKth(self,curr,k):
        while curr and k>0:
            curr = curr.next
            k -=1
        return curr         
