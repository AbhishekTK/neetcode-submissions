class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        m = {}
        M,N = len(grid),len(grid[0])
        v = [[False]*n for _ in range(N)]
        def dfs(i,j,t):
            if (i<0 or j<0 or i>=M or j>=N or v[i][j]):
                return float('inf')
            if i==M-1 and j==N-1:
                return max(t,grid[i][j])
            v[i][j] = True
            t = max(t,grid[i][j])
            r = t
            for dx,dy in d:
                r = min(r,dfs(i+dx,j+dy,t))
            v[i][j]=False
            return r
        return dfs(0,0,0)
            
            
