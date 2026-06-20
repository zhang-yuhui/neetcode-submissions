class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp =[]
        n = len(s)
        m = len(t)
        for i in range(n):
            dp.append([0] * m)
        
        if s[0] == t[0]:
            dp[0][0] = 1
        
        for i in range(1, n):
            for j in range(0, min(i + 1, m)):
                if i < j:
                    continue
                if s[i] == t[j]:
                    if j == 0:
                        dp[i][j] = dp[i - 1][j] + 1
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]