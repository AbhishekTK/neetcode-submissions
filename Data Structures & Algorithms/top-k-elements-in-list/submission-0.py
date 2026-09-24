class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for i in nums:
            if i in memo:
                memo[i] = memo[i]+1
            else:
                memo[i] = 1
        print(memo)
        l = []
        for x,y in memo.items():
            l.append([y,x])
        l.sort(reverse=True)
        print(l)
        res = []
        for e in range(k):
            res.append(l[e][1])
        return res
        # memoSorted = sorted( lambda          