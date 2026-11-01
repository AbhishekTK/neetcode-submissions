class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 =[]
        s2 = []

        for e in s:
            if e =="(":
                s1.append(e)
            elif e=="*":
                s2.append(e)
            else:
                if s1:
                    s1.pop()
                else:
                    s2.pop()
        
        if len(s1)>0:
            return False
        return True
            