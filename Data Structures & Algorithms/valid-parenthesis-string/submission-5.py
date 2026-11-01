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
                if len(s1)>0:
                    s1.pop()
                elif len(s2)>0:
                    s2.pop()
                else:
                    return False
                print(s1)
                print(s2)
                
        
        if len(s1)>0:
            if len(s1)- len(s2)<=0:
                return True
            else:
                return False
        return True
            