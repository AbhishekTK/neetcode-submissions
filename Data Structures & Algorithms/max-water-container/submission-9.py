class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = 0
        n = len(heights)
        for i in range(n):
            for j in range(i+1,n):
                r = max(r, min(heights[j],heights[i])*(j-i)) 
        return r