# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r= []
        def d(n,depth):
            if not n:
                return None
            if len(r)== depth:
                r.append([])
            
            r[depth].append(n.val)
            d(n.left,depth+1)
            d(n.right,depth+1)
        d(root,0)
        return r