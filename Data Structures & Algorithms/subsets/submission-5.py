class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        re = []
        def r(cs,i):
            if i == len(nums):
                re.append(cs.copy())
                return 
            cs.append(nums[i])
            r(cs,i+1)
            cs.pop()
            r(cs,i+1)
        r([],0)
        return re