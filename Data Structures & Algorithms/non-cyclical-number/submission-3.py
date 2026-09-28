class Solution:
    def isHappy(self, n: int) -> bool:
        
        m = set()
        r = 0
        s = n
        while s not in m:
            m.add(s)
            r = 0
            while s:
                r += (s%10)**2
                s //=10
            s = r
            if s==1:
                return True
        # if s==1:
            # return True
        return False