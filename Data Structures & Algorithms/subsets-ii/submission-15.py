class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        def d(i, cur):
            r.append((cur.copy()))
            for j in range(i,len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                cur.append(nums[j])
                d(j+1,cur)
                cur.pop()
                

            # d(i+1,cur)
        d(0,[])
        return r
