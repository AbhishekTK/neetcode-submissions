# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        s = []
        s.append([root])
        # res.append(root)
        while s:
            r = s.pop()
            if not r or len(r)==0:
                break 
            print(r)
            res.append(r[-1].val)
            print(res)
            ss = []
            for e in r:
                if e and e.left:
                    ss.append(e.left)
                if e and e.right:
                    ss.append(e.right)
            
            s.append(ss)
                # ss.append(e)
        return res
            