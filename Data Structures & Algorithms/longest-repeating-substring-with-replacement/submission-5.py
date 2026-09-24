class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res= 0
        for i in range(len(s)):
            memo, maxf = {},0
            for j in range(i,len(s)):
                memo[s[j]] = 1 + memo.get(s[j],0)
                maxf = max(maxf,memo[s[j]])
                if (j-i+1) -maxf<=k:
                    res = max(res,j-i+1)
        return res