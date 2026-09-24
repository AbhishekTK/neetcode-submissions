class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def d(i):
            if i >= n:
                return i==n
            if cache[i] != -1:
                return cache[i]
            cache[i] = d(i+1)+d(i+2)
            return cache[i]
        return d(0)