class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        f,t = 0,0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    f+=1
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        while f>0:
            fl = False

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        for x,y in d:
                            nr = i+x
                            nc = j+y
                            if (nr in range(m) and nc in range(n) 
                                and grid[nr][nc]==1):
                                grid[nr][nc]=3
                                f -= 1
                                fl = True
            if not fl:
                return -1
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==3:
                        grid[i][j]=2
            t +=1
        return t
