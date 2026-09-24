class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        # r = 1
        flag = False
        if not piles or n==0:
            return 0
        # l = mx = max(piles)
        l = 1
        r = mn = max(piles)
        # while l
        res = r
        while l<=r:
            m = (l+r)//2
            t = 0
            for i,banana in enumerate(piles):
                t+= (banana + m-1)//m
            if t<=h:
                res = m
                r = m-1
            else:
                l = m+1

        return res