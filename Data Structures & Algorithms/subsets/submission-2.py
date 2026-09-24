class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        for n in nums:
            r+= [ s +[n] for s in r]
        return r