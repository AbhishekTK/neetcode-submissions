class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        M,N = len(matrix),len(matrix[0])

        def d(r,c,p):
            if (min(r,c)<0 or r>=M or c>=N or matrix[r][c]<=p):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            res = max(res,1+d(r+1,c,matrix[r][c]))
            res = max(res,1+d(r,c+1,matrix[r][c]))
            res = max(res,1+d(r-1,c,matrix[r][c]))
            res = max(res,1+d(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        for i in range(M):
            for j in range(N):
                d(i,j,-1)
        return max(dp.values()) 