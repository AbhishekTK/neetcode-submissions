class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        def d(i,j):

            if i<0 or j<0 or i>=M or j>=N or grid[i][j]!="1":
                return False
            grid[i][j] = "0"
            d(i+1,j)
            d(i,j+1)
            d(i-1,j)
            d(i,j-1)
        r=0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=="1":
                    r+=1
                    d(i,j)
                
        return r
