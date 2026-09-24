class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = set()

        def d(i,ss):
            if i==len(nums):
                r.add(tuple(ss.copy()))
                return
            
            ss.append(nums[i])
            d(i+1,ss)
            ss.pop()
            d(i+1,ss)
        nums.sort()
        d(0,[])
        return list(r)