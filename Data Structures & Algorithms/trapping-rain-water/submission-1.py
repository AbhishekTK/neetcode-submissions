class Solution:
    def trap(self, height: List[int]) -> int:
        # p1,p2 = 0,0
        if not height:
            return 0
        a = 0
        n = len(height)
        for i in range(n):
            l = r = height[i]
            for j in range(i):
                l = max(l,height[j])
            for j in range(i+1,n):
                r = max(r,height[j])
            a += min(l,r) - height[i]
        return a
