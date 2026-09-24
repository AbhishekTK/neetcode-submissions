class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.count = defaultdict(int)
        A = []
        cur = []

        for c in candidates:
            if self.count[c]==0:
                A.append(c)
            self.count[c] += 1 
        self.backtrack(A,target,cur,0)
        return self.res
    
    def backtrack(self, A, target, cur, i):
        if target == 0:
            self.res.append(cur.copy())
            return
        if target<0 or i>=len(A):
            return
        if self.count[A[i]]>0:
            cur.append(A[i])
            self.count[A[i]] -= 1
            # target -= A[i]
            self.backtrack(A,target-A[i],cur,i)
            self.count[A[i]] += 1
            cur.pop()
        self.backtrack(A,target,cur,i+1)
        