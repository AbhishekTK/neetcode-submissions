class Solution:
    
    '''
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        
        inf = 2147483647
        M = len(grid)
        N = len(grid[0])
        n = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        v = set()
        def a(i,j): 
            if(min(i,j)<0 or i>=M or j>=N or (r,c) in v or grid[i][j]==-1):
                return
            v.add((r,c))
            q.append([r,c])

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    q.append([i,j])
                    v.add((i,j))
            dist += 1
        
        d = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = d
                a(r+1,c)
                a(r-1,c)
                a(r,c+1)
                a(r,c-1)
            d += 1
    
    
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] != -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

    '''

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0
        while q:
            # Process one "layer" of distance at a time
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist # This works now because of the layer logic
                
                # Check all 4 directions
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        (nr, nc) not in visit and grid[nr][nc] != -1):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            dist += 1

