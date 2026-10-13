class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        m = {}
        def dfs(i,j):
            if j==n :
                return i==m
            if (i,j) in m:
                return m[(i,j)]
            match = i<m and (s[i]==p[j] or p[j]==".")
            if (j+1)<n and p[j+1]=="*":
                m[(i,j)] (dfs(i,j+2) or (match and dfs(i+1,j)))
                return m[(i,j)]
            if match:
                m[(i,j)] = dfs(i+1,j+1)
                return m[(i,j)]
            m[(i,j)] =  False
            return False
        return dfs(0,0)
            