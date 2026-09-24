class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        a = [[] for _ in range(n+1)]
        def d(n,p):
            if vi[n]:
                return True
            vi[n] = True
            for vo in a[n]:
                if vo==p:
                    continue
                if d(vo,n):
                    return True
            return False
        
        for u,v in edges:
            a[u].append(v)
            a[v].append(u)
            vi = [False]*(n+1)
            if d(u,-1):
                return [u,v]
        return []
