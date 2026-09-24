class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        m = [-1]*n
        def dfs(i):
            if i<0:
                return 0
            if m[i]!=-1:
                return m[i]
            
            m[i]= max(nums[i]+dfs(i-2),dfs(i-1))
            return m[i]

        return dfs(n-1)