class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        # List[List[str]]
        res = []

        for s in strs:
            if str(sorted(s)) in memo:
                memo[str(sorted(s))].append(s)
            else:
                memo[str(sorted(s))] = [s]
        for v in memo.values():
            res.append(v)
        return res
        
        