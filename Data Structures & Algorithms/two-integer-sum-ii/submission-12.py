class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m={}
        for i,n in enumerate(numbers):
            if target- n in m:
                return [m[target-n],i+1]
            m[n]= i+1
        return []