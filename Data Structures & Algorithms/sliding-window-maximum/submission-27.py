class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        lm = [0]*n
        rm = [0]*n
        lm[0] = nums[0]
        rm[n-1] = nums[n-1]
        for i in range(1,n):
            if i%k==0:
                lm[i] = nums[i]
            else:
                lm[i] = max(lm[i-1],nums[i])
            if (n-i-1)%k == 0:
                rm[n-i-1] = nums[n-i-1]
            else:
                rm[n-i-1] = max(nums[n-1-i],rm[n-i])
        op = [0]*(n-k+1)

        for i in range(n-k+1):
            op[i] = max(lm[i+k-1],rm[i])
        return op