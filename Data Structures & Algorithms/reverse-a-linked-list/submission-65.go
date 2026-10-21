/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    var p *ListNode
	c:=head
	for c!=nil{
		t :=c.Next
		c.Next = p
		p = c
		c = t
	}
	return p
}
