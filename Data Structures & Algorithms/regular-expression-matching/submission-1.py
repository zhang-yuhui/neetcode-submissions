class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = []
        n = len(s)
        m = len(p)
        for i in range(n + 1):
            dp.append([False] * (m + 1))
        for i in range(2,m+1,2):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j - 1] == '*':
                    if p[j - 2] in {s[i-1], '.'}:
                        dp[i][j] = dp[i][j - 2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
                    
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    dp[i][j] = False
        
        # print(dp)
        return dp[-1][-1]
                    

