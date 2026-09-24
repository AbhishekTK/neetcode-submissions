class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)<len(text2):
            return self.longestCommonSubsequence(text2,text1)
        l1 = len(text1)
        l2 = len(text2)
        m = [ [0 for _ in range(l2+1)] for _ in range(l1+1)]

        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                if text1[i] ==text2[j]:
                    m[i][j] = 1+m[i+1][j+1]
                else:
                    m[i][j]=max(m[i+1][j],m[i][j+1])
        return m[0][0]