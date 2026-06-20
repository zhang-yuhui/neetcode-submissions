class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = []
        for i in range(n):
            dp.append([0] * (amount + 1))

        for i in range(n):
            dp[i][0] = 1
        for i in range(n):
            for j in range(1, amount + 1):
                k = j
                if i == 0:
                    dp[i][j] = 1 if j % coins[i] == 0 else 0
                    continue
                while k >= 0:
                    dp[i][j] += dp[i - 1][k]
                    k -= coins[i]
                
        #print(dp)
        return dp[-1][-1]

