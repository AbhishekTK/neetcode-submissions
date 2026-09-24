class Solution:
    def climbStairs(self, n: int) -> int:
        s1,s2 = 1,1
        for i in range(2,n+1):
            t = s1+s2
            s1 = s2
            s2 = t
        return s2