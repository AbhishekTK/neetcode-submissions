class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        def d(i, cur):
            if i >= len(nums):
                r.append((cur.copy()))
                return
            cur.append(nums[i])
            d(i+1,cur)
            
            cur.pop()
            while i+1<len(nums) and nums[i]== nums[i+1]:
                i+=1

            d(i+1,cur)
        d(0,[])
        return r
