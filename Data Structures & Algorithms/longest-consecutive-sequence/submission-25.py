class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        m = 0
        cm,c = 0,nums[0]
        n = len(nums)
        i = 0
        while i<n:
            if c!=nums[i]:
                c = nums[i]
                cm = 0
            while i<n and nums[i] == c:
                i+=1
            cm+=1
            c+=1
            m = max(m,cm)
        return m