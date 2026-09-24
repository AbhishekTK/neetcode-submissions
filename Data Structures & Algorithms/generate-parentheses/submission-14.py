class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r= []
        def b(i,ss,c):
            if i == c == n:
                r.append(ss)
                return
            if i<n:
                b(i+1,ss+"(",c)
            if c<n and c<i:
                b(i,ss+")",c+1)
        b(0,"",0)
        return r

