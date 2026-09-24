class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.h(nums[1:]),self.h(nums[:-1]))
    
    def h(self, n):
        r1,r2 = 0,0

        for e in n:
            nr = max(r1+e,r2)
            r1 = r2
            r2 = nr
        return r2