class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t)>len(s):
            return 0
        r = 0
        d = {}
        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in d:
                return d[(i,j)]
            res = dfs(i+1,j)
            if s[i]==t[j] :
                res += dfs(i+1,j+1)
            d[(i,j)] = res
            return res
        return dfs(0,0)
            