class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        def dfs(x, y, cnt, visited, q):
            nonlocal ans
            if cnt == n:
                tmp = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if (i, j) in q:
                            s += 'Q'
                        else:
                            s += '.'

                    tmp.append(s)

                ans.append(tmp)
                return
            
            if x == n or y == n:
                return
            nx = x
            ny = y+1
            if ny == n:
                nx = x+1
                ny = 0
            dfs(nx, ny, cnt, visited.copy(), q.copy())
            if (x, y) not in visited:
                for i in range(n):
                    visited.add((x, i))
                    visited.add((i, y))
                
                for dx, dy in [[-1, 1], [1, 1], [-1,-1], [1, -1]]:
                    tx, ty = x, y
                    while 0 <= tx < n and 0 <= ty < n:
                        visited.add((tx, ty))
                        tx, ty = tx + dx, ty + dy
                q.add((x, y))
                dfs(nx, ny, cnt + 1, visited, q)
        
        dfs(0, 0, 0, set(), set())
        return ans