# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        c = root
        while True:
            if val>c.val:
                if not c.right:
                    c.right = TreeNode(val)
                    return root
                c = c.right
            else:
                if not c.left:
                    c.left = TreeNode(val)
                    return root
                c = c.left
            
