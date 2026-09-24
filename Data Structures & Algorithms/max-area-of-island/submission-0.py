class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        v = set()

        def h(i, j):
            if (i<0 or i>=m or j<0 or j>=n or (grid[i][j] == 0) or ((i,j) in v)):
                return 0
            v.add((i,j))
            return (1+h(i+1,j)+h(i-1,j)+h(i,j+1)+h(i,j-1))

        res= 0
        for i in range(m):
            for j in range(n):
                res = max(res,h(i,j))
        return res
    
    
