import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = np.ones((3,2))
        print(d)
        print(type(d))
        dp = [[1 for _ in range(n)] for _ in range(m)]
        print(dp)
        r,c = 0,0
        rows,cols = m,n
        cache = {}
        def d(r,c):
            if r==rows or c==cols:
                return 0
            if r==m-1 and c==n-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = d(r+1,c)+d(r,c+1)
            return cache[(r,c)]
        
        
        return d(r,c)
        # return dp[m-1][n-1]
        