class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key = lambda interval :interval[0]) 
        r = [intervals[0]]

        for i in intervals[1:]:
            if i[0]<=r[-1][1]:
                r[-1][1]= max(i[1],r[-1][1])
            else:
                r.append(i)
        return r