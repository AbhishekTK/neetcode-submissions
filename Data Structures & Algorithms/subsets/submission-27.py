class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        def d(i,ss):
            if i>=len(nums):
                r.append(ss.copy())
                return
            
            ss.append(nums[i])
            d(i+1,ss)
            ss.pop()
            d(i+1,ss)
        d(0,[])
        return r