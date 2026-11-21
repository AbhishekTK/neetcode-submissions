class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tl = sum(matchsticks)
        if tl%4!=0:
            return False
        l = tl//4

        s = [0]*4
        matchsticks.sort(reverse=True)

        def d(i):

            if i==len(matchsticks):
                return True
            for e in range(4):
                if s[e]+matchsticks[i]<=l:
                    s[e]+=matchsticks[i]
                    if d(i+1):
                        return True
                if s[e]==0:
                    break
            return False
        return d(0)