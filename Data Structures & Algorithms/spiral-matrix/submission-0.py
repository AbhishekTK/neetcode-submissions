class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t,r,b,l = 0,len(matrix[0])-1,len(matrix)-1,0
        c = True
        d = 0
        r = []
        p = 0
        while c:
            if d==0:
                p = l
                while p<= r:
                    r.append(matrix[t][p])
                    p+=1
                d =1
                t+=1
            if d==1:
                p = t
                while p<=b:
                    r.append(matrix[p][r])
                    p+=1
                r-=1
                d=2
            if d==2:
                p = r
                while p<=l:
                    r.append(matrix[b][p])
                    p-=1
                b-=1
                d=3
            if d==3:
                p = b
                while p<=t:
                    r.append(matrix[p][l])
                    p-=1
                d=0
                l+=1
            if t==b:
                c= False
        return r
            