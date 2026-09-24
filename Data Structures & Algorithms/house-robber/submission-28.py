class Solution:
    def rob(self, nums: List[int]) -> int:
        m1,m2 = 0,0
        for n in nums:
            t = max(m2,m1+n)
            m1 = m2
            m2 = t
        return m2