class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = []
        def r(i,ss):
            if i>= len(nums):
                return s.append(ss.copy()) 
            ss.append(nums[i])
            r(i+1,ss)
            ss.pop()
            r(i+1,ss)
        r(0,[])
        return s
            