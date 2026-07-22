class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(pos, cur, n, a):
            nonlocal nums, ans
            length = len(nums)
            if cur == n:
                ans.append(a.copy())
                return
            if length - pos < n - cur:
                return
            dfs(pos + 1, cur, n, a)

            a.append(nums[pos])
            dfs(pos + 1, cur + 1, n, a)
            a.pop()
        
        for i in range(len(nums)+1):
            dfs(0, 0, i, [])
        return ans
            
        