# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(r,sr):
            if not sr and not r:
                return True
            
            if r and sr and r.val==sr.val:
                return dfs(r.left,sr.left) and dfs(r.right,sr.right)
            
            return False
        if not subRoot:
            return True
        if not root:
            return False

        if dfs(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
