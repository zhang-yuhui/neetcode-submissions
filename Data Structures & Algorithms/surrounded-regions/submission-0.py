class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        cell = set()
        O = set()
        
        m = len(board)
        n = len(board[0])
        mark = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    O.add((i,j))
        dir = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(x: int, y: int):
            nonlocal mark
            if mark == True:
                return
            if board[x][y] == 'O':
                cell.add((x,y))
            else:
                return
            for i, j in dir:
                nx = x + i
                ny = y + j
                if nx >= m or ny >= n or nx < 0 or ny < 0:
                    mark = True
                    #print(nx,ny)
                elif board[nx][ny] == 'O' and (nx, ny) not in cell:
                    dfs(nx, ny)

        for (i, j) in O:
            if board[i][j] == 'O':
                dfs(i, j)
                if mark == False:
                    for (x, y) in cell:
                        board[x][y] = 'X'

                cell = set()
                mark = False


            