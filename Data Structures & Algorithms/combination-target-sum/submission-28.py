class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        nums.sort()

        def d(i,cs,t):
            if t==target:
                r.append(cs.copy())
                return
            
            for j in range(i,len(nums)):
                if t+nums[j]>target:
                    return
                cs.append(nums[j])
                d(j,cs,t+nums[j])
                cs.pop()
                # d(i+1,cs,t)
        d(0,[],0)
        return r
            