# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        # s.append(root.val)
        def d(node):
            if not node:
                return
            d(node.left)
            s.append(node.val)
            d(node.right)
        d(root)
        print(s)
        # s.sort()
        return s[k-1] if len(s)>=k else -1
         