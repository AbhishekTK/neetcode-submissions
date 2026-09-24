# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def rec(r):
            if not r:
                return 0

            return 1+max(rec(r.left),rec(r.right))
        
        if not root:
            return True
        
        l= rec(root.left)
        r= rec(root.right)
        if abs(l-r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)