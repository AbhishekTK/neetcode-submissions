# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        s = [[root,1]]
        r = 0

        while s:
            ro,d = s.pop()
            if ro:
                r = max(r,d)
                s.append([ro.left,d+1])
                s.append([ro.right,d+1])
        return r
        