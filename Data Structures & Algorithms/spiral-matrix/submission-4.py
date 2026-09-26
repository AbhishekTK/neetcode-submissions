class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        res = []

        def d(row,col,r,c,dr,dc):
            if row==0 or col==0:
                return 
            for i in range(col):
                r+=dr
                c+=dc
                res.append(matrix[r][c])
            d(col,row-1,r,c,dc,-dr)
        d(m,n,0,-1,0,1)
        return res