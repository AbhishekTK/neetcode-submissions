class Solution:
    def myPow(self, x: float, n: int) -> float:
        def h(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            r = h(x*x,n//2)
            return x*r if n%2 else r
        r = h(x,abs(n))
        return r if n>=0 else 1/r