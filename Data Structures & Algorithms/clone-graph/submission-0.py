"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        o= {}
        def d(n):
            if n in o:
                return o[n]
            c= Node(n.val)
            o[n]= c
            for ne in n.neighbors:
                c.neighbors.append(d(ne))
            return c
        return d(node) if node else None
