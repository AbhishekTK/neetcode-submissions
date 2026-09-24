# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        def b():
            # if not r:
            #     return None
            while q:
                n = q.popleft()
                temp= n.left
                n.left = n.right
                n.right = temp
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        b()
        return root
