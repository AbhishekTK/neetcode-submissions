class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n= len(height)
        lm,rm = [-1]*n,[-1]*n
        for i in range(n):
            if lm[i]==-1 and (i>0 and lm[i-1]>=height[i]):
                lm[i] = lm[i-1]
            else:
                lm[i] = height[i]
        for i in range(n-1,-1,-1):
            if rm[i]==-1 and (i<n-1 and rm[i+1]>=height[i]):
                rm[i] = rm[i+1]
            else:
                rm[i] = height[i]
        print(lm)
        print(rm) 
        for i in range(n):
            res += min(lm[i],rm[i]) - height[i]
        return res       