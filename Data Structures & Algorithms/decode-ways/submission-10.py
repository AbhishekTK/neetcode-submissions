class Solution:
    def numDecodings(self, s: str) -> int:
        m = {}
        def r(i):
            if i== len(s):
                return 1
            if i in m:
                return m[i]
            if s[i]=='0':
                return 0
            res = r(i+1)
            if i<len(s)-1:
                if(s[i]=='1' or s[i]=='2' and s[i+1]<'7'):
                    res += r(i+2)
            m[i] = res
            # res = 0
            # if i+1<len(s) and ( int(s[i:i+1]) <=26 or int(s[i:i+1])>=1):
            #     res =  r(i+1)
            # if i+2<len(s) and ( int(s[i:i+2]) <=26 or int(s[i:i+2])>=10):
            #     res+= r(i+2)
            return res
        return r(0)
            