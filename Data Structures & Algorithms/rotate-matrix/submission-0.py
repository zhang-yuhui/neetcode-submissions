class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def r(x, y):
            return (y, n - 1 - x)
        
        h = n // 2 
        for i in range(h):
            for j in range(h):
                x, y = i, j
                tmp = matrix[x][y]
                x1, y1 = r(x, y)
                tmp1 = matrix[x1][y1]
                x2, y2 = r(x1, y1)
                tmp2 = matrix[x2][y2]
                x3, y3 = r(x2, y2)
                tmp3 = matrix[x3][y3]
                matrix[x][y] = tmp3
                matrix[x1][y1] = tmp
                matrix[x2][y2] = tmp1
                matrix[x3][y3] = tmp2

        if n % 2 == 1:
            for i in range(h):
                x, y = h, i
                tmp = matrix[x][y]
                x1, y1 = r(x, y)
                tmp1 = matrix[x1][y1]
                x2, y2 = r(x1, y1)
                tmp2 = matrix[x2][y2]
                x3, y3 = r(x2, y2)
                tmp3 = matrix[x3][y3]
                matrix[x][y] = tmp3
                matrix[x1][y1] = tmp
                matrix[x2][y2] = tmp1
                matrix[x3][y3] = tmp2


                