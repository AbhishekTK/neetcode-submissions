# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        def inOrder(n):
            if n is None :
                return
            if n.left is not None:
                inOrder(n.left)
                r.append(n.left.val)
            # r.append(n.val)
            if n.right is not None:
                inOrder(n.right)
                r.append(n.right.val)
        inOrder(root)
        return r