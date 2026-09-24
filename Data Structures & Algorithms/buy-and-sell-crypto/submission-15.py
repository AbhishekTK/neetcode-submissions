class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pro = 0
        # l = 0

        # for p in prices:
        #     if p < l :
        #         l = p
        #     pro = max(pro,p - l)
        # return pro
        m = 0

        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j] - prices[i]> m:
                    m = prices[j] - prices[i]
        return m
