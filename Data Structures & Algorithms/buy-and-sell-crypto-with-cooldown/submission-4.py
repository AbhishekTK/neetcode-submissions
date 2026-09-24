class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def d(i,b):
            if i>=len(prices):
                return 0
            if (i,b) in dp:
                return dp[(i,b)]

            c = d(i+1,b)
            if b:
                bu = d(i+1,not b) - prices[i]
                dp[(i,b)] =  max(bu,c)
            else:
                s = d(i+2,not b) +prices[i]
                dp[(i,b)] = max(s,c)
            return dp[(i,b)]
        return d(0,True)