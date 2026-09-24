class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = []

        for i in range(len(nums)-k+1):
            m = nums[i]
            for j in range(i,i+k):
                m = max(m,nums[j])
            r.append(m)
        return r