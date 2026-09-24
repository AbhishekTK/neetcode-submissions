# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        m = [root.val]

        def d(n):
            if not n:
                return 0
            l = d(n.left)
            r = d(n.right)
            l = max(l,0)
            r = max(r,0)
            m[0] = max(m[0], n.val+l+r)
            return n.val+max(l,r)
        d(root)
        return m[0]

            