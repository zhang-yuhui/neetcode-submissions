class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        l = 0
        r = n * m - 1

        while l <= r:
            mid = (l + r) // 2
            a = matrix[l//m][l%m]
            b = matrix[mid//m][mid%m]
            c = matrix[r//m][r%m]

            if target in {a, b, c}:
                return True
            if l == r or r - l == 1:
                return False
            if b > target:
                r = mid
            else:
                l = mid
        
        return False
