class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = 0
        r = []
        while s<=len(nums)-k:
            # l = 
            r.append(max(nums[s:s+k]))
            s +=1
        return r