class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [False]*n
        r = 0
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i):
            # if i in vis:
                # return False
            # vis.add(i)
            for n in adj[i]:
                if not vis[n]:
                    vis[n] = True
                    dfs(n)

        for i in range(n):
            if not vis[i]:
                vis[i] = True
                dfs(i)
                r+=1
        return r