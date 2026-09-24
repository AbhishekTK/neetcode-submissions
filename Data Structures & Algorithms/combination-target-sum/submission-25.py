class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []

        def d(i,cs,t):
            if t==target:
                r.append(cs.copy())
                return
            
            if i>=len(nums) or t>target:
                return
            cs.append(nums[i])
            d(i,cs,t+nums[i])
            cs.pop()
            d(i+1,cs,t)
        d(0,[],0)
        return r
            