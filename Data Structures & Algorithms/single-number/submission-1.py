class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = set()
        for x in nums:
            if x in m:
                m.remove(x)
            else:
                m.add(x)
        return list(m)[0]
        