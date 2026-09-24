class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        k = 0
        pe = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=pe:
                # intervals[i][1] = max(intervals[i-1][1],intervals[i][1])
                pe = intervals[i][1]
            else:
                k+=1
                pe = min(intervals[i][1],pe)
        return k