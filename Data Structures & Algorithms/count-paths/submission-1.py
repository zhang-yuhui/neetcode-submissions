class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([1] * n)
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                x = dp[i-1][j] if i > 0 else 0
                y = dp[i][j-1] if j > 0 else 0
                dp[i][j] = x+y
        return dp[-1][-1]