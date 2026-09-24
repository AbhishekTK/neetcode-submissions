# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        if not root :
            return -1
        s.append(root.val)
        def d(root,s):
            if not root:
                return
            if root.left:
                s.append(root.left.val)
            if root.right:
                s.append(root.right.val)
            d(root.left,s)
            d(root.right,s)
        d(root,s)
        print(s)
        s.sort()
        return s[k-1] if len(s)>=k else -1
         