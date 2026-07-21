class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        t = s // 2
        dp = []
        for i in range(n):
            dp.append([0] * (t+1))
        for i in range(n):
            for j in range(t+1):
                if i == 0:
                    dp[i][j] = 1 if j == nums[i] else 0
                else:
                    dp[i][j] = max(dp[i-1][j-nums[i]], dp[i-1][j]) if j >= nums[i] else  dp[i-1][j]
        
        return dp[-1][t] == 1
