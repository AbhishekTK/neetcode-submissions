class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n ==1:
            return nums[0]
        m = [[-1]*2 for _ in range(n)]
        
        def d(i,f,n):
            if i>=n or (f and i==n-1):
                return 0
            if m[i][f]!=-1:
                return m[i][f]
            m[i][f] = max(nums[i]+d(i+2,f ,n),d(i+1,f,n))
            return m[i][f]
        return max(d(0,True,n),d(1,False,n))