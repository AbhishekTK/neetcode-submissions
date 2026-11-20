class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # res = []
        m = {0:1}
        nums.sort()
        def r(total):
            if total ==0:
                return 1
            res = 0
            for i in range(len(nums)):
                if total<nums[i]:
                    break
                res += r(total-nums[i])
            return res
        return r(target)