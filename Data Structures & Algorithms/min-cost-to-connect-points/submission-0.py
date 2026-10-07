class DSU:
    def __init__(self,n):
        self.Parent = list(range(n+1))
        self.Size = [1]*(n+1)
    def find(self,node):
        if self.Parent[node]!=node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu==pv:
            return False
        if self.Size[pu]<self.Size[pv]:
            pu,pv = pv,pu
        self.Size[pu]+=self.Size[pv]
        self.Parent[pv] = pu
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        e = []
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                d = abs(x1-x2)+abs(y1-y2)
                e.append((d,i,j))
        e.sort()
        r = 0
        for d,u,v in e:
            if dsu.union(u,v):
                r+=d
        return r