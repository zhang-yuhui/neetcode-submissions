class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(x, y):
            nonlocal grid, n, m
            if grid[x][y] == "0":
                return
            pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            grid[x][y] = "0"
            for dx, dy in pos:
                nx , ny = x + dx, y+dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] == "1":
                    dfs(nx, ny)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    print(i, j)
                    dfs(i, j)
                    ans += 1
        return ans