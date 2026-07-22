class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [0] * n
        for i in range(n):
            if i == 0:
                if s[i] == '0':
                    return 0
                else:
                    dp[i] = 1
                continue

            x = s[i]
            if x == '0':
                if s[i-1] not in {'1', '2'}:
                    dp[i] = 0
                else:
                    dp[i] = dp[i-2] if i != 1 else 1

            else:
                dp[i] = dp[i-1]
                if s[i-1] in {'1', '2'} and int(s[i-1]+x) <= 26:
                    dp[i] +=( dp[i-2] if i != 1 else 1)

        print(dp)
        return dp[-1]
                
