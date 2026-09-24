class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        if t == "":
            return ""
        ms,mt = {},{}
        for e in t:
            mt[e] = 1+mt.get(e,0)
        h,n = 0,len(mt)
        resi,resl = [0,0],float("infinity")
        for r in range(len(s)):
            e = s[r]
            ms[e] = 1+ms.get(e,0)
            if e in mt and mt[e]==ms[e]:
                h+=1
            while h ==n:
                if (r-l+1)<resl:
                    resl = r-l+1
                    resi = [l,r]
                ms[s[l]] -=1
                if s[l] in mt and ms[s[l]]<mt[s[l]]:
                    h -=1
                l+=1

        l,r = resi
        return s[l:r+1] if resl < float("infinity") else ""