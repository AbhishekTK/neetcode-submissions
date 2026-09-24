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
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            d(i+1,ss)
        nums.sort()
        d(0,[])
        return list(r)