class ST:
    def __init__(self,N,A):
        self.n = N
        while (self.n & (self.n-1)) !=0:
            self.n +=1
        self.build(N,A)
    def build(self,N,A):
        self.t = [float('-inf')]* (2*self.n)
        for i in range(N):
            self.t[i+self.n] = A[i]
        for i in range(self.n-1,0,-1):
            self.t[i] = max(self.t[i<<1],self.t[i<<1|1])
    def query(self,l,r):
        l += self.n
        r += self.n+1
        res = float('-inf')
        while l<r:
            if l&1:
                res = max(res,self.t[l])
                l+=1
            if r&1:
                r-=1
                res = max(res,self.t[r])
            l >>=1
            r >>=1
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = ST(len(nums),nums)
        op = []
        for i in range(len(nums)-k+1):
            op.append(s.query(i,i+k-1))
        return op