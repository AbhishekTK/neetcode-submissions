# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res =0

        def d(n):
            nonlocal res
            if not n:
                return 0
            lm = d(n.left)
            rm = d(n.right)
            res = max(res,lm +rm)
            return 1+max(lm,rm)
            
        d(root)
        return res
            