class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c = len(grid),len(grid[0])
        # v = [[False]*c for _ in range(r)]

        def d(i,j):
            t = [[0,1],[0,-1],[1,0],[-1,0]]
            if (i<0 or j<0 or i>=r or j>=c or grid[i][j]=="0"):
                return 
            # if not v[i][j]:
            grid[i][j] = "0"
            
            for e in t:
                print(e)
                d(i+e[0],j+e[1])
            # return 1

        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    print(i,j)
                    d(i,j)
                    res += 1
        return res
