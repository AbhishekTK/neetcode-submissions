class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        m = {}
        def r(i,c):
            if (i,c) in m:
                return m[(i,c)]
            if i==len(nums):
                return 1 if c==target else 0
            
            if i>=len(nums):
                return 0
            m[(i,c)] =  r(i+1,c-nums[i])+r(i+1,c+nums[i])
            return m[(i,c)]
        return r(0,0)
