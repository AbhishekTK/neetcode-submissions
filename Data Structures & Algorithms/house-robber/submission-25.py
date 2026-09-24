class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]
        n = len(nums)
        m = [-1]*n
        m[0] = nums[0]
        m[1] = max(nums[1],nums[0])

        for i in range(2,n):
            m[i] = max(m[i-1],nums[i]+m[i-2])
            
        
        return m[n-1]