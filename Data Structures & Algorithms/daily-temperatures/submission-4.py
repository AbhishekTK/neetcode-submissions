class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0]* len(temperatures)
        print(r)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    r[i] = j-i
                    break
        return r