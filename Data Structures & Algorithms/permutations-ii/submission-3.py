class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                s.add(tuple(perm))
                return
            for i in range(len(nums)):
                if nums[i]!= float("-inf"):
                    perm.append(nums[i])
                    nums[i] = float("-inf")
                    backtrack(perm)
                    nums[i] = perm[-1]
                    perm.pop()
        backtrack([])
        return list(s)
            
            