class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp = {}

        def d(i,j,k):
            if k == len(s3):
                return (i==len(s1) and j==len(s2))
            if (i,j) in dp:
                return dp[(i,j)]
            
            r = False
            if i<len(s1) and s1[i]==s3[k]:
                r =  d(i+1,j,k+1)
            if j<len(s2) and s2[j]==s3[k]:
                r =  d(i,j+1,k+1)
            dp[(i,j)] = r
            return r
        return d(0,0,0)
