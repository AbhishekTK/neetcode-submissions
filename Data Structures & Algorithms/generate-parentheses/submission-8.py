class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        r = []

        def b(o,c):
            if o == c == n:
                r.append("".join(s))
                return
            if o<n:
                s.append("(")
                b(o+1,c)
                s.pop()
            if c<o:
                s.append(")")
                b(o,c+1)
                s.pop()
            
        b(0,0)
        return r