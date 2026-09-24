# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {e:i for i,e in enumerate(inorder)}
        self.pre_idx = 0
        def d(l,r):
            if l>r:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx +=1 
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = d(l,mid-1)
            root.right = d(mid+1,r)
            return root
        return  d(0,len(preorder)-1)
