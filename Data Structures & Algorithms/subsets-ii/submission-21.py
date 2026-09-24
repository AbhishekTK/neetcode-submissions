class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        nums.sort()
        idx = prev_idx = 0
        for i in range(len(nums)):
            idx = prev_idx if i>=1 and nums[i] == nums[i-1] else 0
            prev_idx = len(r)
            for j in range(idx,prev_idx):
                t = r[j].copy()
                t.append(nums[i])
                r.append(t)

        return r