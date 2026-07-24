class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = []
        n = len(nums)
        nums.sort()
        ans = []
        def dfs(pos, cur_sum, cur_number):
            nonlocal ans
            if cur_sum == target:
                ans.append(cur_number.copy())
                return
            if pos >= n:
                return
            
            remain = target - cur_sum
            if remain < nums[pos]:
                return
            tmp = 0
            while cur_sum <= target:
                dfs(pos+1, cur_sum, cur_number)
                cur_sum += nums[pos]
                cur_number.append(nums[pos])
                tmp += 1
            for i in range(tmp):
                cur_sum -= nums[pos]
                cur_number.pop()
        
        dfs(0, 0, [])
        return ans
            
            