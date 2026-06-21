class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = []
        n = len(heights)
        m = len(heights[0])

        for i in range(n):
            grid.append([0] * m)

        for i in range(n):
            grid[i][0] += 1
            grid[i][-1] += 2
        
        for i in range(m - 1):
            grid[0][i + 1] += 1
            grid[-1][i] += 2
        #print(grid[-1][-1])
        pos = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def bfs(x, y, mark):
            nonlocal grid
            pq = [(x, y)]
            while pq:
                x, y = pq.pop()
                for dx, dy in pos:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if grid[nx][ny] == 3 or grid[nx][ny] == mark:
                        continue
                    if heights[x][y] <= heights[nx][ny]:
                        grid[nx][ny] += mark
                        pq.append((nx, ny))
        
        for i in range(n):
            bfs(i, 0, 1)
            bfs(i, m-1, 2)
        
        for i in range(m):
            bfs(0, i, 1)
            bfs(n-1, i, 2)
        
        ans = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 3:
                    ans.append([i, j])
        #print(grid)
        return ans

