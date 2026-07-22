class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(board)
        m = len(board[0])
        visited = []
        for i in range(n):
            visited.append([0]*m)
        def dfs(x, y, cur):
            if cur == len(word) - 1 and word[cur] == board[x][y]:
                return True
            if word[cur] != board[x][y]:
                return False
            visited[x][y] = 1
            res = False
            for dx, dy in [[1,0],[-1,0],[0, 1], [0, -1]]:
                nx = dx+x
                ny = dy+y
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    res = res or dfs(nx, ny, cur + 1)
            visited[x][y] = 0
            return res
        ans = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    ans = ans or dfs(i, j, 0)
        
        return ans