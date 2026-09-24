class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        l = 0
        se = set()
        for r in range(n):
            while s[r] in se:
                se.remove(s[l])
                l += 1
            se.add(s[r])
            res = max(res,len(se))
        return res