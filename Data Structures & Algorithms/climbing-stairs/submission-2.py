class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]*(n+1)
        if n<=2:
            return n
        res[2],res[1]=2,1
        for j in range(3,(n)+1):
            res[j]= res[j-1]+res[j-2]
        return res[n]