class Solution:
    def isHappy(self, n: int) -> bool:
        
        m = set()
        r = 0
        s = n
        while s ==1 or s in m:
            m.add(r)
            r = 0
            while s:
                r += (s%10)**2
                s //=10
            s = r
        if s==1:
            return True
        return False