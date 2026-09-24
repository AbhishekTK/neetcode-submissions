class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}
        def r(i):
            if i in m:
                return m[i]
            if i>=n:
                return i==n
            m[i]=r(i+1)+r(i+2)
            return m[i]
        return r(0)