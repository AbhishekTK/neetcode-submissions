class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = 0
        m,n = len(grid),len(grid[0])
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        def d(i,j,m,n):
            grid[i][j]="0"
            for dx,dy in dir:
                di=i+dx
                dj= j+dy
                if (di<0 or dj<0 or di>=m or dj>=n or grid[di][dj]=="0"):
                    continue
                d(di,dj,m,n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    d(i,j,m,n)
                    r+=1
        return r