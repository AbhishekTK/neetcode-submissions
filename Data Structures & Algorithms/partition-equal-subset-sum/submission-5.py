class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums)
        if t%2!=0:
            return False
        tar = t//2
        m = [[-1]*(tar+1) for _ in range(len(nums))]

        def d(i,t):
            if i==len(nums):
                return t==0
            if i>=len(nums) or tar<0:
                return False
            if m[i][t]!=-1:
                return m[i][t]
            m[i][t] = d(i+1,t) or d(i+1,t-nums[i])
            return m[i][t]
        return d(0,tar)
