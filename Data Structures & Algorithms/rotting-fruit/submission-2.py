from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])
        visited = set()
        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                count += grid[r][c] == 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        if count == 0:
            return 0
        
        minutes = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS
                    or grid[nr][nc] == 0 or (nr, nc) in visited):
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    count -= 1
            minutes += 1
        
        return minutes if count == 0 else -1
                
