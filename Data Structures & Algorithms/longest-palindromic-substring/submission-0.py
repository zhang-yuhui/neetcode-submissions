class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = []
        for i in range(n):
            dp.append([0] * n)
        for l in range(n):
            for i in range(n):
                if i + l >= n:
                    break

                if l == 0: # length 1
                    dp[i][i] = 1
                elif l == 1: # length 2
                    dp[i][i + l] = 2 if s[i] == s[i + 1] else 0
                else:
                    if dp[i + 1][i + l - 1] == l - 1 and s[i] == s[i + l]:
                        dp[i][i + l] = dp[i + 1][i + l - 1] + 2
        ans = [0,0,0]
        for i in range(n):
            for j in range(n):
                if dp[i][j] > ans[0]:
                    ans[0] = dp[i][j]
                    ans[1], ans[2] = i, j

        if ans[0] > 0:
            return s[ans[1]:ans[2] + 1]
        else:
            return ''