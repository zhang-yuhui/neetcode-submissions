class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur = 0
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        pos = [0, 0]
        while len(ans) < m * n:
            ans.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = -10000000
            nx = pos[0] + dir[cur][0]
            ny = pos[1] + dir[cur][1]
            if nx >= m or nx < 0 or ny >= n or ny < 0 or matrix[nx][ny] == -10000000:
                cur = (cur + 1) % 4
                nx = pos[0] + dir[cur][0]
                ny = pos[1] + dir[cur][1]
            
            pos[0], pos[1] = nx, ny

        return ans