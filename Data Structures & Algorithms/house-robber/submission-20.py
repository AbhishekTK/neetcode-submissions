class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def r(i,n):
            if i>=n:
                return 0
            if i ==n -1:
                return nums[i]
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i]+r(i+2,n),r(i+1,n)) 
            return memo[i]
        
        return r(0,n)


            