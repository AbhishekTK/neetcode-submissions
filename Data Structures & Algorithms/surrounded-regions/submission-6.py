class Solution:
    def solve(self, board: List[List[str]]) -> None:
        di = [[1,0],[-1,0],[0,1],[0,-1]]
        M,N = len(board),len(board[0])
        def df(i,j):

            if (min(i,j)<0 or i>=M or j >=N or board[i][j]!= "O"):
                print(board)
                print(i,j)
                return
            board[i][j] = "T"
            print(board)
            df(i+1,j)
            df(i-1,j)
            df(i,j+1)
            df(i,j-1)
        
        for r in range(M):
            if board[r][0] =="O":
                df(r,0)
            if board[r][N-1] == "O":
                df(r,N-1)
        for c in range(N):
            if board[0][c] =="O":
                df(0,c)
            if board[M-1][c] == "O":
                df(M-1,c)
        for r in range(M):
            for c in range(N):
                if board[r][c] =="O":
                    board[r][c] = "X"
                    print(board)
                elif board[r][c] == "T":
                    board[r][c] = "O"
                    print(board)
        
        