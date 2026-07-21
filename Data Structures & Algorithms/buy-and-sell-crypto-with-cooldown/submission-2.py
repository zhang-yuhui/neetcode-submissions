class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = []
        for i in range(n):
            dp.append([0,0,0])
        
        for i in range(n):
            if i == 0:
                dp[0][0] = -prices[0]
                dp[0][-1] = -float('inf')
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0] + prices[i] 
        
        ans = -1
        for i in range(n):
            ans = max(ans, max(dp[i]))

        return ans
        