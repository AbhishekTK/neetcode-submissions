class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}

        for c in s:
            if c in m:
                m[c] +=1
            else:
                m[c] =1

        for c in t:
            if c in m:
                m[c] -=1
            else:
                return False
        # a = False
        for k,v in m.items():
            if v !=0:
                return False
        return True 

        