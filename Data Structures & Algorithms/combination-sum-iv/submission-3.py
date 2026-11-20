class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        # m = {}
        nums.sort()
        def r(total):
            if total ==0:
                return 1
            res = 0
            for i in range(len(nums)):
                if total<nums[i]:
                    break
                res += dfs(i,total-nums[i])
        return r(target)