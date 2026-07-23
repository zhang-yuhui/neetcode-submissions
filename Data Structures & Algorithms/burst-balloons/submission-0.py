class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = []
        n = len(nums)
        for i in range(n):
            dp.append([0] * n)
        
        for l in range(1, n+1):
            for i in range(n):
                j = i+l-1
                if j >= n:
                    break
                left = nums[i-1] if i > 0 else 1
                right = nums[j + 1] if j < n-1 else 1
                p = left * right
                if i == j:
                    dp[i][j] = nums[i] * p
                else:
                    for k in range(i, j+1):
                        tmp = nums[k] * p
                        if k != i:
                            tmp += dp[i][k-1]
                        if k != j:
                            tmp += dp[k + 1][j]
                        dp[i][j] = max(dp[i][j], tmp)
        return dp[0][-1]