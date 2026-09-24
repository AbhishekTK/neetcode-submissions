class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        sii = 0
        m  = False
        n = len(intervals)
        r = []
        ii=0
        while ii < n and intervals[ii][1]<newInterval[0]:
            r.append(intervals[ii])
            ii+=1
        
        while ii<n and intervals[ii][0]<=newInterval[1]:
                newInterval[0] = min(intervals[ii][0],newInterval[0])
                newInterval[1] = max(intervals[ii][1],newInterval[1])
                ii+=1
                # intervals[ii] = [si,ei]
        r.append(newInterval)
        
        while ii<n :
            r.append(intervals[ii])
            ii+=1


        return r