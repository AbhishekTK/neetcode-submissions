class Solution:
    def isValid(self, s: str) -> bool:
        r = 0
        st = []
        for p in s:
            if p=='{' or p=='(' or p=='[':
                r+=1
                st.append(p)
            else:
                if st:
                    cp = st.pop()
                    if (cp == "(" and p!=")") or (cp == "[" and p!="]") or (cp == "{" and p!="}"):
                        return False
                else:
                    return False
                r-=1
        return True and r==0