class TrieNode:
    def __init__(self):
        self.c = [None]*26;
        self.i = -1;
        self.r = 0;
    def addWord(self,w,i):
        c = self
        c.r+=1
        for ch in w:
            ind = ord(ch)-ord('a')
            if not c.c[ind]:
                c.c[ind]=TrieNode()
            c = c.c[ind]
            c.r+=1
        c.i=i
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root= TrieNode()
        for i in range(len(words)):
            root.addWord(words[i],i)
        R,C =len(board),len(board[0])
        res = []

        def gi(c):
            i = ord(c)-ord('a')
            return i
        def d(r,c,n):
            if(r<0 or c<0 or r>=R or c>=C or board[r][c]=='*' or not n.c[gi(board[r][c])]):
                return 0
            t = board[r][c]
            board[r][c]='*'
            p = n
            n = n.c[gi(t)]
            f = 0
            if n.i !=-1:
                res.append(words[n.i])
                n.i = -1
                f+=1
            f+=d(r+1,c,n)
            f+=d(r-1,c,n)
            f+=d(r,c+1,n)
            f+=d(r,c-1,n)
            board[r][c]=t
            if not n.r:
                p.c[gi(t)]=None
            return f
        for r in range(R):
            for c in range(C):
                root.r -=d(r,c,root)
        return res




