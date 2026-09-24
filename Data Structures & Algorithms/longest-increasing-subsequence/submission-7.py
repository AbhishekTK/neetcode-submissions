class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        m= [[-1]*(n+1) for _ in range(n)]
        def d(i,j):
            if i==n:
                return 0
            if m[i][j+1]!=-1:
                return m[i][j+1]
            
            LIS = d(i+1,j)

            if j==-1 or nums[j]<nums[i]:
                LIS = max(LIS,1+d(i+1,i))
            m[i][j+1] =LIS
            return LIS
        return d(0,-1) 
            
