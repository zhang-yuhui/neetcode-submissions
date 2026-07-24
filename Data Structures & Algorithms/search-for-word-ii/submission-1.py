class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = {}
        for w in words:
            cur = tree
            l = len(w)
            for i in range(l):
                if w[i] not in cur:
                    cur[w[i]] = {}
                cur = cur[w[i]]
            cur['*'] = w
        
        visited = set()
        n = len(board)
        m = len(board[0])
        ans = set()
        def dfs(x, y, cur):
            nonlocal visited, ans
            
            if board[x][y] not in cur:
                return
            if '*' in cur[board[x][y]]:
                ans.add(cur[board[x][y]]['*'])
            visited.add((x, y))
            for dx, dy in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                nx = dx+x
                ny = dy+y
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    dfs(nx, ny, cur[board[x][y]])
            visited.remove((x, y))
        for i in range(n):
            for j in range(m):
                visited.clear()
                if board[i][j] in tree:
                    dfs(i, j, tree)
        
        return list(ans)
            
            