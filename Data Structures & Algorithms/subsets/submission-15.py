class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = []
        for i in range(1<<n):
            ss = [nums[j] for j in range(n) if (i & (1<<j))]
            s.append(ss)
            
        return s            