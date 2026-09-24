class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        prev = 1
        total = 1
        for i in range(n-1):
            temp = total
            total = prev + total
            prev = temp
        return total 