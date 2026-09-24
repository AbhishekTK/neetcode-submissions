class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for _ in range(n)]
        print(b)
        def ba(r):
            if r == n:
                copy = ["".join(row) for row in b]
                res.append(copy)
                return
            for c in range(n):
                if self.isSafe(r,c,b):
                    b[r][c] = "Q"
                    ba(r+1)
                    b[r][c] = "."
        ba(0)
        return res
    def isSafe(self,r,c,b):
        row = r-1
        while row>=0:
            if b[row][c]=="Q":
                return False
            row -=1
        
        row,col = r-1,c-1
        while row>=0 and col>=0:
            if b[row][col] == "Q":
                return False
            row -=1
            col-=1
        row,col = r-1,c+1
        while row>=0 and col<len(b):
            if b[row][col] == "Q":
                return False
            row -=1
            col+=1
        return True