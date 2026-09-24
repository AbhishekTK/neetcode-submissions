# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root ==None:
                return 0
                ## and root.left == None and root.right== None:
                ## return 0
            
            return 1+max(dfs(root.left),dfs(root.right))
        if not root:
            return 0
        l= dfs(root.left)
        r= dfs(root.right)
        d = l+r
        s = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(d,s)