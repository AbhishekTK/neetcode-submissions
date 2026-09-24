class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {}
        for i,e in enumerate(nums):
            if target - e in m:
                return [m[target-e],i]
            m[e] = i
        return []