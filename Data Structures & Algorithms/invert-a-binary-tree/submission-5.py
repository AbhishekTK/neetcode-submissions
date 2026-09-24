# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def d(n):
            if not n:
                return None
            temp= n.left
            n.left = n.right
            n.right = temp
            d(n.left)
            d(n.right)
        d(root)
        return root
