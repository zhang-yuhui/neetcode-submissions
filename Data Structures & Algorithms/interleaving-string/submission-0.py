class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if len(s3) != m + n:
            return False
        dp = []
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                tmp.append([False, False])
            dp.append(tmp)
        dp[0][0] = [True, True]
        for i in range(m):
            if s1[i] == s3[i]:
                dp[i+1][0][0] = True
            else:
                break
        
        for i in range(n):
            if s2[i] == s3[i]:
                dp[0][i+1][1] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1,n+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j][0] = dp[i-1][j][0]  or dp[i-1][j][1]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j][1] = dp[i][j-1][1] or dp[i][j-1][0]
        
        return dp[-1][-1][0] or dp[-1][-1][1]
                

                
        
        
        
        