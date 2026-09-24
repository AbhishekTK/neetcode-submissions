/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
    if head==nil{
        return
    }
    l := []*ListNode{}
    c := head
    for c!=nil{
        l= append(l,c)
        c= c.Next
    }

    i, j := 0, len(l)-1
    for i<j{
        l[i].Next = l[j]
        i++
        if i>=j {break}
        l[j].Next = l[i]
        j--
    }
    l[i].Next = nil
}
