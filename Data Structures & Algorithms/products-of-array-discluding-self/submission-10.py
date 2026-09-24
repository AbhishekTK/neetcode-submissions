class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod , zc = 1,0
        for i in nums:
            if i:
                prod *= i
            else:
                zc += 1
            if zc > 1: return [0]*len(nums)
        
        res = [1]* len(nums)
        for i,c in enumerate(nums):
            if zc: res[i] = 0 if c else prod
            else:
                res[i] = prod//c
        return res