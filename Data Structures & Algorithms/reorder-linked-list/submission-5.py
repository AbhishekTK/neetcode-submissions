# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # l1,l2 = head,head
        # while l2:
        #     l1 = l1.next
        #     l2 = l2.next.next
        
        # # t = ListNode
        # t= head
        # d = t

        # while t != l1:
        if not head:
            return
        a = []
        t = head
        while t:
            a.append(t)
            t = t.next
        i,j = 0,len(a)-1
        while i<j:
            a[i].next = a[j]
            i+=1
            if i>=j:
                break
            a[j].next=a[i]
            j-=1
        a[i].next = None
        # return a[0]
