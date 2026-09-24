class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0 
        n = len(prices)
        # l = 0
        # while l < len(prices):
        for i in range(n):
            for j in range(i+1,n):
                d = prices[j] - prices[i]
                m = max(m,d)
        return m