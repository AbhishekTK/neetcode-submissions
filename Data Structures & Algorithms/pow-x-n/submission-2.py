class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        r = 1
        for i in range(abs(n)):
            r*=x
        return r if n>=0 else 1/r
        