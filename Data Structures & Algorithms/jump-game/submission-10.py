class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [False]*n
        memo[-1] = True

        for i in range(n-2,-1,-1):
            end = min(n,i+nums[i]+1)
            for j in range(i+1,end):
                if memo[j]:
                    memo[i] = True
                    break
        return memo[0]


        