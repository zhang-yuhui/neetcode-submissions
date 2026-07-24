class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        low = [prices[0]]
        high = [prices[-1]]
        for i in range(1, n):
            low.append(min(low[-1], prices[i]))
            high.append(max(high[-1], prices[n-i-1]))
        high.reverse()
        ans = 0
        for i in range(n):
            ans = max(ans, high[i]-low[i])
        return ans