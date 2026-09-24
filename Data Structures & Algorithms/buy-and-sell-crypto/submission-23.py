class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        r = 0
        for p in range(1,len(prices)):
            if m>prices[p]:
                m = prices[p]
            r = max(r,prices[p]-m)
        return r
