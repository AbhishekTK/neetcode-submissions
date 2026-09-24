class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        l,r = 0,n-1

        while l<=r:
            m = (l+r)//2
            if intervals[m][0]<newInterval[0]:
                l = m+1
            else:
                r = m-1
        
        intervals.insert(l,newInterval)

        for i in intervals:
            if not res or res[-1][1]< i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1],i[1])
        return res
            