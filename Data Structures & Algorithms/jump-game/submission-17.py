class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = {}
        def d(i):
            if i in m:
                return m[i]
            if i==len(nums)-1:
                return True
            if nums[i]==0:
                return False
            e = min(len(nums)-1, i+nums[i])
            for j in range(i+1,e+1):
                if d(j):
                    m[j] = True
                    return True
            m[j] = False
            return False
        return d(0)