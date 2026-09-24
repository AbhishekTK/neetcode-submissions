class Solution:
    def countBits(self, n: int) -> List[int]:
        c = []
        for i in range(n+1):
            t = 0
            d = i
            for j in range(i):
                if (1 << j) & d:
                    t += 1
            c.append(t)
        return c