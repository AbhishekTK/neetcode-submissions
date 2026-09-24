class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = [[]]
        for n in nums:
            s += [subset +[n] for subset in s]
        return s            