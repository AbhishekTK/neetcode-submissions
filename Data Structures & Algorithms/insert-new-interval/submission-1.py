class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        op = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
               op.append(newInterval)
               return op + intervals[i:] 
            elif newInterval[0] > intervals[i][1]:
                op.append(intervals[i])
            else:
                newInterval[0] = min(intervals[i][0],newInterval[0])
                newInterval[1] = max(intervals[i][1],newInterval[1])
        op.append(newInterval)
        return op
