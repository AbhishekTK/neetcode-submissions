# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        s = deque([root])
        r = []
        while s:
            n = s.popleft()
            if not n:
                r.append("N")
            else:
                r.append(str(n.val))
                s.append(n.left)
                s.append(n.right)
        return ",".join(r)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        r = TreeNode(int(vals[0]))
        q = deque([r])
        i = 1
        while q:
            n = q.popleft()
            if vals[i]!="N":
                n.left = TreeNode(int(vals[i]))
                q.append(n.left) 
            i+=1
            if vals[i]!="N":
                n.right = TreeNode(int(vals[i]))
                q.append(n.right)
            i+=1
        return r