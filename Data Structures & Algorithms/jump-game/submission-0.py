class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        n = len(nums)
        for i in range(n):
            if pos < i:
                return False
            pos = max(pos, i + nums[i])
        
        return True