class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        memo = {}
        def r(i):
            if i>=len(nums):
                return 0
            if i ==len(nums) -1:
                return nums[i]
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i]+r(i+2),r(i+1)) 
            return memo[i]
        
        return r(0)


            