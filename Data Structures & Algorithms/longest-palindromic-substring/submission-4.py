class Solution:
    def longestPalindrome(self, s: str) -> str:
        sn = len(s)
        dp =[[False]*(sn) for _ in range(sn)]
        ri,rl=0,0
        m = ""


        def p(i,j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i,j= i+1,j-1
            return True

        for i in range(sn-1,-1,-1):
            for j in range(i,sn):
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1] ):
                    dp[i][j] = True
                    if rl <(j-i+1):
                        ri = i
                        rl = j-i+1
                
        return s[ri:ri+rl]