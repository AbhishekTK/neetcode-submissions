class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r= []
        nums.sort()

        def d(i,c,t):
            if target==t:
                r.append(c.copy())
                return 
            for j in range(i,len(nums)):
                if t + nums[j]>target:
                    return
                c.append(nums[j])
                d(j,c,t+nums[j])
                c.pop()
            
        d(0,[],0)
        return r