class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        n = len(nums)
        for i in range(1,n):
            dp[i] = max(dp[i], dp[i]+dp[i-1])
        return max(dp)