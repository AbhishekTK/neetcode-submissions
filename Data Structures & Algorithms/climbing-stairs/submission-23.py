class Solution:
    def climbStairs(self, n: int) -> int:
        
        m = [0]*(n+1)
        m[0],m[1]=1,1
        i = 0
        def d(i):
            if i==0:
                return 1
            if m[i]!= 0:
                return m[i]
            m[i] = d(i-1)+d(i-2)
            return m[i]
        return d(n+1)
        