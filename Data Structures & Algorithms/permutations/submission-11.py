class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def r(s):
            if s == len(nums):
                res.append(nums[:])
                return

            for i in range(s,len(nums)):
                nums[s], nums[i] = nums[i], nums[s]
                r(s+1)
                nums[s], nums[i] = nums[i], nums[s]
        r(0)
        return res 
