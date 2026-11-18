class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mte = {}
        mtr = {}
        for truster,trustee in trust:
            mte[trustee] = mte.get(trustee,0)+1
            mtr[truster]=mtr.get(trustee,0)+1 
        print(mte)
        print(mtr)
        for i in range(1,n+1):
            print(i)
            print(i in mte  and i not in mtr )
            if i in mte and mte[i] == n and i not in mtr :
                return i
        return -1