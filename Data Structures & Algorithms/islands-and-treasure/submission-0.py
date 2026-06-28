from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n, m, = len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            x, y, dis = q.popleft()
            pos =[[1,0],[0,1],[-1,0],[0,-1]]
            for dx, dy in pos:
                nx, ny = x+dx, y+dy
                if nx < n and ny < m and nx >=0 and ny >=0 and grid[nx][ny] > dis + 1:
                    q.append((nx, ny, dis+1))
                    grid[nx][ny] = dis + 1
        