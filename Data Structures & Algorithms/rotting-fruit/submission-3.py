"""
0 = empty
1 = fresh fruit
2 = rotten fruit 

time counter
multi source bfs 
    add all rotten oranges
for each rotten orange:
    traverse neighbors 
    rotten fresh fruit, 1s
    increment timer 

keep track of fresh oranges in case one is not connected to a rotten orange
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if not rows or not cols:
            return -1

        visited = set()
        time, fresh = 0, 0
        q = deque()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in dirs:
                    nr, nc = r + x, c + y
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            print("one queue iteration done, curr q:", q)
            time += 1

        return time if fresh == 0 else -1



