class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r=min(strs)
        for i in range(len(min(strs))):
            for j in strs:
                if j[i]!=r[i]:
                    return r[:i]
        return r