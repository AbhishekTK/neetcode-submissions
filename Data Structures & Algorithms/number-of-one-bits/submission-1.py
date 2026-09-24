class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for i in range(32):
            mask = 1 << i
            if mask & n != 0 :
                c += 1
        return c