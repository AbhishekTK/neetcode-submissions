# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = -float('inf')
        def d(n):
            nonlocal m
            if not n:
                return
            l = self.max(n.left)
            r = self.max(n.right)
            m = max(m,n.val+l+r)
            d(n.left)
            d(n.right)
        d(root)
        return m

    def max(self,n):
        if not n:
            return 0
        l = self.max(n.left)
        r = self.max(n.right)
        m = n.val+max(l,r)
        return max(0,m)
