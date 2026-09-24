class Solution:
    def climbStairs(self, n: int) -> int:
        sr5 = math.sqrt(5)
        phi = (1+sr5)/2
        psi = (1-sr5)/2
        n+=1
        return round((phi**n-psi**n)/sr5)