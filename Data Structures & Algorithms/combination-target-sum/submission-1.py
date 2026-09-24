class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r= [
        ]
        def d(i,c,t):
            if target==t:
                r.append(c.copy())
                return 
            if i>=len(nums) or t> target:
                return
            c.append(nums[i])
            d(i,c,t+nums[i])
            c.pop()
            d(i+1,c,t)
        d(0,[],0)
        return r