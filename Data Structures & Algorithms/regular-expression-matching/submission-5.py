class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M,N = len(s),len(p)
        m = {}
        def dfs(i,j):
            if j==N :
                return i==M
            if (i,j) in m:
                return m[(i,j)]
            match = i<M and (s[i]==p[j] or p[j]==".")
            if (j+1)<N and p[j+1]=="*":
                m[(i,j)]= (dfs(i,j+2) or (match and dfs(i+1,j)))
                return m[(i,j)]
            if match:
                m[(i,j)] = dfs(i+1,j+1)
                return m[(i,j)]
            m[(i,j)] =  False
            return False
        return dfs(0,0)
            