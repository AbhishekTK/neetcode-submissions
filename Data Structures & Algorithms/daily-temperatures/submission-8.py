class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        r = [0]*n
        s = []

        for i,t in enumerate(temperatures):
            while s and t>s[-1][0]:
                st,si = s.pop()
                r[si] = i -si
            s.append((t,i))
        return r