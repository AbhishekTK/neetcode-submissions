class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp =[*nums]
        for j in range(1,len(nums)):
            dp[j] = max(nums[j], nums[j]+dp[j-1])
        return max(dp)