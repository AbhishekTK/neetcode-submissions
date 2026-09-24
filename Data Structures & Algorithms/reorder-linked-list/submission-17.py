# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        c = head
        while c:
            l.append(c)
            c = c.next
        # r = ListNod
        le,r= 0,len(l)-1
        while le<r:
            l[le].next = l[r]
            le+=1
            if le>=r:
                break
            l[r].next = l[le]
            r-=1
        l[le].next= None
        # return l[0]