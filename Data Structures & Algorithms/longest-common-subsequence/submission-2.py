class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = {}

        def r(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if (i,j) in m:
                return m[(i,j)]
            
            if text1[i]==text2[j]:
                m[(i,j)] = 1+r(i+1,j+1)
            else:
                m[(i,j)] = max(r(i,j+1),r(i+1,j))
            return m[(i,j)]
        return r(0,0)