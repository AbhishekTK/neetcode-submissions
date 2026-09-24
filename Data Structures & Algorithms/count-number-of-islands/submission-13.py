class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # s = []
        r,c = len(grid),len(grid[0])
        res = 0
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(i,j):
            s = deque()
            grid[i][j] = "0"
            s.append((i,j))
            while s:
                ii,jj = s.popleft()
                for di,dj in d:
                    dr,dc = ii+di,jj+dj
                    if (dr<0 or dc<0 or dr>=r or dc>=c or grid[dr][dc]== "0"):
                        continue    
                    s.append((dr,dc))
                    grid[dr][dc] = "0"
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    bfs(i,j)
                    res += 1
        return res