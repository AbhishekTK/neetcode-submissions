class Solution:
    def rob(self, nums: List[int]) -> int:
        m = [-1]* (len(nums))
        #m[0]= 0
        def dfs(i):
            if i >= len(nums):
                return 0
            if m[i] != -1:
                return m[i]
            m[i]= max(dfs(i+1),dfs(i+2)+nums[i])
            '''
            return max(dfs(i+1),nums[i]+ dfs(i+2))
            '''
            return m[i]
        return dfs(0)