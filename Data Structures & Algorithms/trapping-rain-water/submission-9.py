class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n= len(height)
        lm,rm = [-1]*n,[-1]*n
        lm[0] = height[0]
        for i in range(1,n):
            lm[i] = max(lm[i-1],height[i])
        rm[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rm[i] = max(rm[i+1],height[i])
        for i in range(n):
            res += min(lm[i],rm[i]) - height[i]
        return res       