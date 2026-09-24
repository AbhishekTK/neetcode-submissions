class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=j=0
        m = {}
        for idx,e in enumerate(nums):
            if target-e in m:
                return [m[target-e],idx]
            m[e] = idx
        return -1 