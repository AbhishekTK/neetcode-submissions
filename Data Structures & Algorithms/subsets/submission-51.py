class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # s = set()
        r = [[]]

        for n in nums:
            r += [ rs+[n] for rs in r]
        return r