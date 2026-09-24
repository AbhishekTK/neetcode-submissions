class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0]*len(temperatures)
        s = []

        for i,t in enumerate(temperatures):
            while s and t>s[-1][1]:
                si,st = s.pop()
                r[si] = i - si
            s.append((i,t))
        return r  