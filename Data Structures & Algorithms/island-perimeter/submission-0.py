class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        v = set()
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        M,N = len(grid),len(grid[0])
        def dfs(i,j):
            if max(i,j)<0 or i>=M or j>=N or grid[i][j]==0:

                return 1
            if (i,j) in v:
                return 0
            
            v.add((i,j))
            p = 0
            for dx,dy in d:
                p+= dfs(i+dx,j+dy)
            return p
        
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    return dfs(i,j)
        return 9
            