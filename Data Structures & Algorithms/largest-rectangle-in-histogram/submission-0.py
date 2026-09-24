class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        a = 0
        n = len(heights)
        for i in range(n):
            h = heights[i]
            r = i + 1
            while r < n and heights[r] >= h:
                r += 1
            l = i 
            while l >= 0 and heights[l] >= h:
                l -= 1
            r -= 1
            l += 1
            a = max (a, h * (r - l + 1))
        
        return a