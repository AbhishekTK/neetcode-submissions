class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1,p2 = 0,0
        m = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                m = max(m, (j-i)*min(heights[i],heights[j]))
        return m
