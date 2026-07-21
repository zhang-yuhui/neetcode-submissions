class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if target < -s or target > s:
            return 0
        dp = []
        for i in range(n):
            dp.append([0] * (s*2+1))
        for i in range(n):
            for j in range(-s, s+1):
                if i == 0:
                    dp[i][j] = 1 if abs(j) == nums[i] else 0
                    if j == 0 and nums[i] == 0:
                        dp[i][j] += 1
                else:
                    dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
        #print(dp[0])
        return dp[-1][target]
        
