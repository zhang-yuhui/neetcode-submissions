class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0
        pos = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        def dfs(x, y):
            nonlocal area, grid
            if grid[x][y] == 1:
                grid[x][y] = 0
                area += 1
            else:
                return
            
            for dx, dy in pos:
                nx, ny = dx+x, dy+y
                if nx >= 0 and ny >= 0 and nx < n and ny < m and grid[nx][ny] == 1:
                    dfs(nx, ny)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    ans = max(ans, area)


        return ans