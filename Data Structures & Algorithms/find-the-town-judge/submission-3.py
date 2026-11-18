class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mte = {}
        mtr = {}
        for truster,trustee in trust:
            mte[trustee] = mte.get(trustee,0)+1
            mtr[truster]=mtr.get(trustee,0)+1 

        for i in range(1,n+1):
            if mte[i] == n-1 and mtr[i] == 0:
                return i
        return -1