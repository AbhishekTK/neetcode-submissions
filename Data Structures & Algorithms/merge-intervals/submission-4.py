class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda a: a[0])
        r = []
        for i in intervals:
            if not r or r[-1][1]<i[0]:
                r.append(i)
            else:
                r[-1][1] = max(i[1],r[-1][1])
        return r
