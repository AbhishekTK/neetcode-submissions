# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        r = []

        def d(node):
            if not node:
                r.append("N")
                return
            r.append(str(node.val))
            d(node.left)
            d(node.right)
        d(root)
        return ",".join(r)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        s = data.split(",")
        self.i = 0
        def d():
            if s[self.i]=="N":
                self.i +=1
                return None
            n = TreeNode(int(s[self.i]))
            self.i += 1
            n.left = d()
            n.right = d()
            return n
        return d()