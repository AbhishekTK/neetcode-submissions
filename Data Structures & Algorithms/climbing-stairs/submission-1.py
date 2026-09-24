class Solution:
    def climbStairs(self, n: int) -> int:
        res= [ 0] *(n+1)
        if n<=2:
            return n
        res[1],res[2] = 1,2
        for i in range(3,n+1):
            res[i]= res[i-1]+res[i-2]
        return res[n]