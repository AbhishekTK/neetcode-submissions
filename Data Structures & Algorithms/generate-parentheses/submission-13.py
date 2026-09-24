class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        c,res = [],[]
        def d(l,r):

            if r == n:
                res.append("".join(c))
                return
            if l<n:
                c.append("(")
                l+=1
                d(l,r)
                c.pop()
                l-=1
            if r<l:
                c.append(")")
                r +=1
                d(l,r)
                r-=1
                c.pop()
        d(0,0)
        return res
            