class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        r = []
        p = []
        def isP(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l,r = l+1,r-1
            return True

        def d(i):
            if i>=len(s):
                # if i ==j:
                r.append(p.copy())
                return
            for j in range(i,len(s)):
                if isP(i,j):
                    p.append(s[i:j+1])
                    d(j+1)
                    p.pop()


            # if isP(s,j,i):
            #     p.append(s[j:i+1])
            #     d(i+1,i+1)
            #     p.pop()
            # d(j,i+1)
            
        d(0)
        return r