class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []

        def d(i,s,ss):
            if s==target:
                r.append(ss.copy())
                return
            if i>=len(nums)or s>target:
                return
            # s += nums[i]
            ss.append(nums[i])
            d(i,s+nums[i],ss)
            ss.pop()
            d(i+1,s,ss)
        d(0,0,[])
        return r