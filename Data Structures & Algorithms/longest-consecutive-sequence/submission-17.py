class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = 0
        s = set(nums)
        for n in s:
            if not (n-1) in s:
                k = n
                while n in s:
                    n+=1
                    
                c = max(n-k,c)
        return c
    
