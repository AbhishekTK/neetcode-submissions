class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = {}
        def r(i,b):
            if i>=len(prices):
                return 0
            if (i,b) in m:
                return m[(i,b)]
            res = r(i+1,b)

            if b:
                res = max(res,prices[i]+r(i+1,False))
            else:
                res = max(res,-prices[i]+r(i+1,True))
            m[(i,b)] = res
            return res
        
        return r(0,False)