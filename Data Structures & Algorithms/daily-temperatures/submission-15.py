class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        r = []
        for i,t in enumerate(temperatures):
            while (s.peak()[0]<t):
                s.pop()
                r.append(i)
            s.append([t,i])
        return r
        