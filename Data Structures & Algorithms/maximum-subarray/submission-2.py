class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        res = nums[0]
        maxSubArrayEnding = nums[0]
        for i in range(1,len(nums)):
            maxSubArrayEnding = max(maxSubArrayEnding+nums[i],nums[i])
            res = max(maxSubArrayEnding,res)
        
        return res
        