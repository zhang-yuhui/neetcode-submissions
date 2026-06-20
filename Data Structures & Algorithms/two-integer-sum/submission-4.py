import bisect
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def find(a:list[int], x):
            idx = -1
            idx2 = -1
            for i in range(len(a)):
                if a[i] == x and idx == -1:
                    idx = i
                elif a[i] == x:
                    idx2 = i
            return idx, idx2
        original = nums.copy()
        nums.sort()
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if x == y:
                if i != 0 and nums[i - 1] == y:
                    return [i - 1,i]
                if i != len(nums) - 1 and nums[i + 1] == y:
                    tmp, tmp2 = find(original, x)
                    return [tmp, tmp2]
            else:
                idx = bisect.bisect_left(nums, y)
                if idx < len(nums) and idx >= 0 and nums[idx] == y:
                    tmp = find(original, x)[0]
                    tmp2 = find(original, y)[0]
                    return [min(tmp, tmp2),max(tmp, tmp2)]
            
        
        return [0,0]