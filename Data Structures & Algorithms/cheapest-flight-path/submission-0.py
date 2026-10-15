class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF]*(k+5) for _ in range(n)]
        for u,v,c in flights:
            adj[u].append([v,c])
        
        dist[src][0] = 0
        minHeap = [(0,src,-1)]
        while len(minHeap):
            c,n,s = heapq.heappop(minHeap)
            if dst == n: return c
            if s==k or dist[n][s+1]<c:
                continue
            for nei,w in adj[n]:
                nc = c+w
                ns = 1+s
                if dist[nei][ns+1]>nc:
                    dist[nei][ns+1]=nc
                    heapq.heappush(minHeap,(nc,nei,ns))
        return -1