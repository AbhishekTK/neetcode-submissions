class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = {}
        re = 0
        l = 0
        r = 0
        for r in range(len(s)):
            if s[r] in se:
                l = max(se[s[r]]+1,l)
                # l += 1
            se[s[r]] = r
            re = max(re,r-l+1)
        return re