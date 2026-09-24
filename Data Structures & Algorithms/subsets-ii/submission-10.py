class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = set()
        nums.sort()
        def d(i, cur):
            if i >= len(nums):
                r.add(tuple(cur.copy()))
                return
            cur.append(nums[i])
            d(i+1,cur)
            cur.pop()
            d(i+1,cur)
        d(0,[])
        return [list(e) for e in r]