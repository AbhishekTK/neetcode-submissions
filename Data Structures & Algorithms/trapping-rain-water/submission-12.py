class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        s = []
        res  = 0

        for i in range((n)):
            while s and height[s[-1]]<height[i]:
                mid = height[s.pop()]
                if s:
                    h = min(height[s[-1]],height[i])-mid
                    w = i -s[-1] -1
                    res += h*w
            s.append(i)
        return res