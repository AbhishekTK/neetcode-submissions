class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        mt = {}
        for c in t:
            mt[c] = 1+ mt.get(c,0)
        res,reslen= [-1,-1] ,float("infinity")
        for i in range(len(s)):
            ms = {}
            for j in range(i,len(s)):
                flag = True
                ms[s[j]] = 1+ms.get(s[j],0)
                for c in mt:
                    if mt[c]> ms.get(c,0):
                        flag = False
                        break
                if flag and (j-i+1)<reslen:
                    reslen = j-i+1
                    res = [i,j]
        l,r = res
        return s[l:r+1] if reslen!=float("infinity") else ""