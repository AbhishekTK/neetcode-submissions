# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # m = root.val
        def d(n,m):
            if not n:
                return 0
            
            r = 1 if n.val >= m else 0
            m = max(m,n.val)
            r += d(n.left,m)
            r += d(n.right,m)

            return r
        return d(root,root.val) 

        