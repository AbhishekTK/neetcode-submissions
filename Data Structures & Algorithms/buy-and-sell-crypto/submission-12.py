class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0 
        n = len(prices)
        # l = 0
        # while l < len(prices):
        l = 0
        mi = prices[0]
        # mx = 
        r = 1
        while r < n:
            if prices[r]> prices[l]:
                m = max(m,prices[r]-prices[l])
                # mi = min(mi,prices[r])
            else:
                l = r
            r +=1
        return m
