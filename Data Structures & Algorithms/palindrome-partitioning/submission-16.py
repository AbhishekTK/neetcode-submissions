class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r,p = [],[]
        
        def b(j,i):
            if i>=len(s):
                if i==j:
                    r.append(p.copy()) 
                return
            if self.isP(s,j,i):
                p.append(s[j:i+1])
                b(i+1,i+1)
                p.pop()
                # print(p)
            # print(p)
            b(j,i+1)
            # print(p)
        b(0,0)
        return r
    def isP(self,s,l,r):
            # l,r = 0,len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l,r = l+1,r-1
            return True