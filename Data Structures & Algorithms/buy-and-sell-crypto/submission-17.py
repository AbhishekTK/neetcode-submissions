class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        m = 0
        for r in prices:
            if r<l:
                l = r
            if r>l:
                m = max(m,r-l)
        return m