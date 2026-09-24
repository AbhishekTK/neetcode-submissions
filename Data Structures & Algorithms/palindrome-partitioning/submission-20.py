class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r, p = [],[]
        def isp(j,i):
            while j<i:
                if s[j]!=s[i]:
                    return False
                j,i = j+1,i-1
            return True
        
        def d(j,i):
            if i>=len(s):
                if j==i:
                    r.append(p.copy())
                return
            if isp(j,i):
                p.append(s[j:i+1])
                d(i+1,i+1)
                p.pop()
            d(j,i+1)
        d(0,0)
        return r