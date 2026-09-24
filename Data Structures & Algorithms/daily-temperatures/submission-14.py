class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        s = []

        for i,t in enumerate(temperatures):
            while s and t> s[-1][0]:
                sT,sI = s.pop()
                
                res[sI] = i-sI
            s.append((t,i))
        return res