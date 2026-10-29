class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0
        def r(i,b):
            if i>=len(prices):
                return 0
            res = r(i+1,b)

            if b:
                res = max(res,prices[i]+rec(i+1,False))
            else:
                res = max(res,-prices[i]+rec(i+1,True))
            return res
        
        return r(0,False)