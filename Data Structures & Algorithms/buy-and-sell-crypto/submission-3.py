class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        right = left
        globalMax = 0
        min = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min:
                min = prices[i]
            
            if prices[i] - min > globalMax:
                globalMax = prices[i] - min

            # if prices[i] - left > currentMax:
            #     currentMax
        return globalMax