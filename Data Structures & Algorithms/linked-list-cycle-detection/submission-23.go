/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
    f,ff := head,head
	for ff!=nil && ff.Next!=nil{
		f =f.Next
		ff = ff.Next.Next
		if f==ff{
			return true

		}
	}
	return false
}
