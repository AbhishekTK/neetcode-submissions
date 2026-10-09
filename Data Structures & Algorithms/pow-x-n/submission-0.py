class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<-1:
            return (1/x)*myPow(x,n+1)
        else:
            return x*myPow(x,n-1)
        