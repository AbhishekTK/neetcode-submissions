class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        m = {}
        def r(i,ss):
            if i>=len(nums) or sum(ss)>target:
                return
            if sum(ss)==target:
                res.append(ss.copy())
                # m[ss[]]
                return
            ss.append(nums[i])
            r(i,ss)
            ss.pop()
            r(i+1,ss)
        r(0,[])
        print(res)
        return len(res)
