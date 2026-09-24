class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        def b(i,cs):
            if i==len(nums):
                r.append(cs.copy())
                return
            cs.append(nums[i])
            b(i+1,cs)
            cs.pop()
            b(i+1,cs)
        b(0,[])
        return r