class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def r(i,c,ss):
            if i>n:
                return
            if c==k:
                res.append(ss.copy())
                return 
            
            ss.append(i)
            r(i+1,c+1,ss)
            ss.pop()
            r(i+1,c,ss)
        res = []
        r(1,0,[])
        return res