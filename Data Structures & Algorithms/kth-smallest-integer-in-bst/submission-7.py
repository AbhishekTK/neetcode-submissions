# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = root
        s = []
        while s or c:
            while c:
                s.append(c)
                c = c.left
            c = s.pop()
            k -= 1
            if k == 0:
                return c.val
            c = c.right
         