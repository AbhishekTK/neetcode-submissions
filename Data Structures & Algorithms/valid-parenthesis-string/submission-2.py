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
                print(s1)
                print(s2)
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    return False
        
        if len(s1)>0:
            return False
        return True
            