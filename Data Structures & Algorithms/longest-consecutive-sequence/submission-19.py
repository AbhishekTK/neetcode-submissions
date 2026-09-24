class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = 0
        d = defaultdict(int)
        for n in nums:
            if not d[n]:
                d[n] = d[n-1] + d[n+1] + 1
                d[n - d[n-1]] = d[n]
                d[n+ d[n+1]] = d[n]
                c = max(c, d[n])
        return c
    
