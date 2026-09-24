class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])

        def d(i,j,w):
            if w == len(word):
                return True
            if (min(i,j)<0 or i>=m or j>=n or board[i][j]!=word[w] or
                board[i][j] == "#"):
                return False
            
            board[i][j] = '#'
            r = d(i+1,j,w+1) or d(i-1,j,w+1) or d(i,j+1,w+1) or d(i,j-1,w+1)
            board[i][j] = word[w]
            return r
        for r in range(m):
            for c in range(n):
                if d(r,c,0):
                    return True
        return False
