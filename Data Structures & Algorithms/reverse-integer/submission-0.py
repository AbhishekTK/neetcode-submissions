class Solution:
    def reverse(self, x: int) -> int:
        t= x
        a= abs(x)
        r= int(str(a)[::-1])
        if t<0:
            r*= -1
        if r<-(1<<31) or r>(1<<31):
            return 0
        return r