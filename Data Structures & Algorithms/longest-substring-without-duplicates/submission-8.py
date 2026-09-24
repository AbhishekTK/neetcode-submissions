class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        re = 0
        l = 0
        r = 0
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l += 1
            se.add(s[r])
            re = max(re,r-l+1)
        return re