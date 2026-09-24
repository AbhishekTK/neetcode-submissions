class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights),len(heights[0])
        dir = [ [1,0],[-1,0],[0,1],[0,-1]]
        pmemo = [[False]*C for _ in range(R) ]
        amemo = [[False]*C for _ in range(R) ]
        
        def b(p,o):
            d = deque(p)
            while d:
                r,c  =  d.popleft()
                o[r][c] = True
                for dr,dc in dir:
                    m,n = r+dr,c+dc
                    if (0<=m<R and 0<=n<C and not o[m][n] and heights[m][n]>=heights[r][c] ):
                        d.append((m,n))
        
        p= []
        a = []
        for i in range(C):
            p.append((0,i))
            a.append((R-1,i))
        for i in range(R):
            p.append((i,0))
            a.append((i,C-1))
        
        b(p,pmemo)
        b(a,amemo)
        res= []
        for r in range(R):
            for c in range(C):
                if pmemo[r][c] and amemo[r][c]:
                    res.append([r,c])
        return res

            



         



        

        
                
