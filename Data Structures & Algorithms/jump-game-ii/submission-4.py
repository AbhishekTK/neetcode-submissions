class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        m = {}
        def r(i):
            if i in m:
                return m[i]
            if i==n-1:
                return 0
            if nums[i]==0:
                return float('inf')
            
            end = min(len(nums)-1,i+nums[i])
            res = float('inf')

            for j in range(i+1,end+1):
                res = min(res,1+r(j))
            m[i] = res
            return res
        return r(0)