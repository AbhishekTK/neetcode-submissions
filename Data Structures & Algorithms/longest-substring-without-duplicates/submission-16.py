class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        l = 0
        m = {}
        for r in range(n):
            # m[s[r]] = 1+ m.get(s[r],0)
            if s[r] in m:
                l = max(m[s[r]]+1,l)
            # se.add(s[r])
            m[s[r]] = r
            res = max(res,r-l+1)
        return res