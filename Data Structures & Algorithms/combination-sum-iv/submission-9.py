class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # res = []
        m = {0:1}
        nums.sort()
        def r(total):
            if total in m:
                return m[total]
            res = 0
            for i in range(len(nums)):
                if total<nums[i]:
                    break
                res+=r(total-nums[i])
                print(res)
                print(m)
            m[total]=res
            print("")
            print(m)
            return res
        return r(target)