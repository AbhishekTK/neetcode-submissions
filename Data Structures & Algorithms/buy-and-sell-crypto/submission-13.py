class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m =0
        mB = prices[0]

        for p in prices:
            m = max(m,p-mB)
            mB = min(mB,p)
        return m
        