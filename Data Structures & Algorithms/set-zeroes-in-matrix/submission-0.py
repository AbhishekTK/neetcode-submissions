class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        M,N = len(matrix),len(matrix[0])
        rz,cz = [1]*M,[1]*N

        for i in range(M):
            for j in range(N):
                if matrix[i][j]==0:
                    rz[i] = 0
                    cz[j] = 0
        for i in range(M):
            for j in range(N):
                if rz[i]==0 or cz[j]==0:
                    matrix[i][j] = 0
        # return 
        