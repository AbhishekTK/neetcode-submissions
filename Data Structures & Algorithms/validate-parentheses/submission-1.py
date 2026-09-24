class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                l.append(c) 
            else:
                if len(l) == 0:
                    return False
                cc = l.pop()
                if (cc == '(' and c != ')' ) or (cc == '[' and c != ']' ) or (cc == '{' and c != '}' ):
                    return False
        if len(l)>0:
            return False
        return True
        