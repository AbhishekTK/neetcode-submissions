class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = set()
        
        def d(i,s):
            if i==len(nums):
                r.add(tuple(s))
                return
            s.append(nums[i])
            d(i+1,s)
            s.pop()
            d(i+1,s)
        nums.sort()
        d(0,[])
        return [list(s) for s in r]
        