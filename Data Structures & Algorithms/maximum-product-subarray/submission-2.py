class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0

        def fd(start, end):
            nonlocal nums
            tmp, ans = 1, min(nums[start:end + 1])
            for i in range(start, end + 1):
                tmp *= nums[i]
                ans = max(ans, tmp)
            tmp = 1
            for i in range(end, start + 1, -1):
                tmp *= nums[i]
                ans = max(ans, tmp)

            return ans
        ans = max(nums)
        for i in range(n):
            if nums[i] == 0 and i != 0:
                ans = max(ans, fd(start, i - 1))
                start = i + 1
            elif i == n - 1:
                ans = max(ans, fd(start, n - 1))
                
        return ans
            