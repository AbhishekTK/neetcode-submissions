class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def r(nums,i,res,s):
            if i>=len(nums):
                res.append(s.copy())
                return
            s.append(nums[i])
            r(nums,i+1,res,s)
            s.remove(nums[i])
            r(nums,i+1,res,s)
        
        res,s=[],[]
        r(nums,0,res,s)
        return res
