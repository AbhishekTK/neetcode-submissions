class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        m = {}
        M,N = len(grid),len(grid[0])

        v = [[False]*N for _ in range(M)]
        minH,maxH = grid[0][0],grid[0][0]
        for r in grid:
            minH = min(minH,min(r))
            maxH = max(maxH,max(r))

        def dfs(i,j,t):
            if (i<0 or j<0 or i>=M or j>=N or v[i][j] or grid[i][j]>t):
                return False
            if i==M-1 and j==N-1:
                return True
            v[i][j] = True
            f = False
            for dx,dy in d:
                f = f or dfs(i+dx,j+dy,t)
            return f

        for t in range(minH,maxH):
            if dfs(0,0,t):
                return t
            for r in range(M):
                for c in range(N):
                    v[r][c]=False
        return maxH