class Solution:
    def climbStairs(self, n: int) -> int:
        m = [-1]*(n+1)
        m[0] = 1
        m[1] = 1
        if n<2:
            return m[n]
        for stair in range(2,n+1):
            m[stair] = m[stair-2]+m[stair-1]
        return m[n]