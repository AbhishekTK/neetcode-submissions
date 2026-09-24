class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = [-s for s in stones]
        m = max(stones)
        b = [0]*(m+1)
        for s in stones:
            b[s] += 1
        f= s= m
        while f>0:
            if b[f]%2==0:
                f-=1
                continue
            j = min(f-1,s)
            while j>0 and b[j]==0:
                j -=1
            if j==0:
                return f
            s = j
            b[f]-=1
            b[s]-=1
            b[f-s] +=1
            f = max(f-1,s)
        return f

        