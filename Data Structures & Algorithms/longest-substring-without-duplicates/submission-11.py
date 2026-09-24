class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        n = len(s)
        for i in range(n):
            se = set()
            for j in range(i,n):
                if s[j] in se:
                    break
                se.add(s[j])
            r = max(r,len(se))
        return r