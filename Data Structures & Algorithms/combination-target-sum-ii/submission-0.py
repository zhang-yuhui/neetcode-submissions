class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            candidates.sort()
            nums = {}
            for i in candidates:
                if i in nums:
                    nums[i] += 1
                else:
                    nums[i] = 1
            a = list(nums.keys())
            n = len(a)
            
            ans = []
            def dfs(pos, cur_sum, numbers):
                nonlocal ans
                if cur_sum == target:
                    ans.append(numbers.copy())
                    return
                if pos >= n:
                    return
                remain = target - cur_sum
                if remain < a[pos]:
                    return
                tmp = 0
                while tmp <= nums[a[pos]] and cur_sum <= target:
                    dfs(pos+1, cur_sum, numbers)
                    cur_sum += a[pos]
                    numbers.append(a[pos])
                    tmp += 1
                for i in range(tmp):
                    cur_sum -= a[pos]
                    numbers.pop()
            dfs(0, 0, [])
            return ans
                
