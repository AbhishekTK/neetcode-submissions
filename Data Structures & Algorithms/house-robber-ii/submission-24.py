class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.r(nums[1:]),self.r(nums[:-1]))
    
    def r(self,nums):

        
        m1,m2 = 0,0
        
        for n in nums:
            t = max(n+m1,m2)
            m1 = m2
            m2 = t
        return m2