# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = k
        r = root.val
        def d(n):
            nonlocal c,r
            if not n:
                return
            d(n.left)
            if c==0:
                return
            c -=1
            if c==0:
                r = n.val
                return
            d(n.right)
        d(root)
        return r