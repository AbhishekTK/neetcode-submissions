class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c = [ set() for i in range(len(board))]
        r = [ set() for i in range(len(board))]
        sub = [ set() for i in range(len(board))]
        # sub = [[0] for i in range(3) for i in range]
        for i in range(len(board)):
            for j in range(len(board[0])):
                    if board[i][j] == '.':
                        continue
                    s = ((i//3)*3+j//3)
                    num = board[i][j]
                    if num in r[i] or num in c[j] or num in sub[s]:
                        return False # Duplicate found
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    print("r["+str(i)+"]",r[i])
                    print("c["+str(j)+"]",c[j])
                    # s = ((i//3)*3+j//3)
                    sub[s].add(board[i][j])
                    print("sub["+str(s)+"]",sub[s])
                
        return True
                

        