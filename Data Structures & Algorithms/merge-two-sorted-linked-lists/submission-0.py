class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        dummy = r
        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                n = list2
                dummy.next = n
                list2 = list2.next
            else:
                n = list1
                dummy.next = n
                list1 = list1.next
            dummy = dummy.next
        if list1 != None:
            dummy.next = list1
        else:
            dummy.next = list2
        return r.next