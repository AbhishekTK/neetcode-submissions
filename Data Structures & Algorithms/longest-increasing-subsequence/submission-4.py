class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = {}

        def d(i):
            # if i>=len(nums):
            #     return 0
            if i in m:
                return m[i]
            LIS = 1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS = max(LIS,1+d(j))
            m[i] = LIS
            return LIS
        return max(d(i) for i in range(len(nums)))
