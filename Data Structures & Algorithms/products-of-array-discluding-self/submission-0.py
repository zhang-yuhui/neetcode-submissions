class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        head = [1] * n
        head[0] = nums[0]
        tail = [1] * n
        tail[-1] = nums[-1]
        for i in range(1, n):
            head[i] = nums[i] * head[i - 1]
            tail[n - i - 1] = nums[n - i - 1] * tail[n - i]

        ans = []
        ans.append(tail[1])
        for i in range(1, n-1):
            ans.append(head[i-1] * tail[i+1])
        ans.append(head[-2])

        return ans