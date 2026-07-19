class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # text1 = ''.join(sorted(text1))
        # text2 = ''.join(sorted(text2))
        dp = []
        for i in range(n):
            dp.append([0]*m)
        
        for i in range(n):
            for j in range(m):
                check = 0 if text1[i] != text2[j] else 1
                if j == 0:
                    dp[i][j] = max(dp[i-1][j], check) if i != 0 else check
                elif i == 0:
                    dp[i][j] = max(dp[i][j-1], check)
                else:
                    if check == 1:
                        dp[i][j] = max(dp[i-1][j-1]+1,dp[i][j-1] ,dp[i-1][j])
                    else:
                        dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])
        return dp[-1][-1]