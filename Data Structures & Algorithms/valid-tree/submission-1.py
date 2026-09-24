class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        v = set()
        def dfs(n,p):
            if n in v:
                return False
            v.add(n)
            for nei in adj[n]:
                if nei== p:
                    continue
                if not dfs(nei,n):
                    return False
            return True
        return dfs(0,-1) and len(v) == n