class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = [[None]*2 for _ in range(len(nums))]
        n = len(nums)
        def r(i,f):

            if i==n-1:
                return max(0,nums[i]) if f else nums[i]
            if m[i][f] is not None:
                return m[i][f]
            if f:
                m[i][f] = max(0,nums[i]+r(i+1,True))
            else:
                m[i][f] = max(r(i+1,False),nums[i]+r(i+1,True))
            return m[i][f]
        return r(0,False)