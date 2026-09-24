class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        m = set()
        mx = 0
        for r in range(len(s)):
            while s[r] in m:
                m.remove(s[l])
                l += 1
            m.add(s[r])
            mx = max(mx,r-l+1)
        return mx
        