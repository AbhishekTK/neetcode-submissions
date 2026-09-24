class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            diff = - nums[i]
            seen = set()
            for j in range(i+1, len(nums)):
                target = diff - nums[j]
                if target in seen:
                    res.add(tuple(sorted([target, nums[i], nums[j]])))
                seen.add(nums[j])
        return [list(x) for x in res]
    

