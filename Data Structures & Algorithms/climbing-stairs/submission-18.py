class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1

        l1,l2 = 1,1
        for i in range(2,n+1):
            t = l1+l2
            l1 = l2
            l2 = t
        return l2
