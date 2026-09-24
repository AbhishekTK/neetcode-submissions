class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        r = [[0]*n for _ in range(n)]
        t = [[0]*n for _ in range(n)]
         
        for i in range(n):
            for j in range(n):
                t[j][i] = matrix[i][j]
        print(t)
                
        for i in range(n):
            for j in range(n):
                r[j][n-1-i] = matrix[i][j]
        print(r)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = r[i][j]
        print(matrix) 