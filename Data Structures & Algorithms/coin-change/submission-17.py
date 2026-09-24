class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = {}
        def d(a):
            if a==0:
                return 0
            if a in m:
                return m[a]
            r = 1e9
            for c in coins:
                if a-c>=0:
                    r = min(r, 1+d(a-c))
            m[a] = r
            return r
        r = d(amount)
        return -1 if r>=1e9 else r
