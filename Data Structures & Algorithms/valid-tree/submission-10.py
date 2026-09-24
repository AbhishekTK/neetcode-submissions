class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)> n-1:
            return False
        
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        v = set()
        q = deque([(0,-1)])
        v.add(0)
        while q:
            node,p = q.popleft()
            for nei in adj[node]:
                if nei == p:
                    continue
                if nei in v:
                    return False
                v.add(nei)
                q.append((nei,node))

        return len(v)== n