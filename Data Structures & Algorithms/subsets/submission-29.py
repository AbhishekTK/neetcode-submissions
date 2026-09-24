class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = [[]]

        for n in nums:
            r += [ ss +[n] for ss in r]
        return r