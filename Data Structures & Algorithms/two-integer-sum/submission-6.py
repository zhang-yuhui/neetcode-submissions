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
            return [idx, idx2]
        d = {}
        n = len(nums)
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        for i in nums:
            y = target - i
            if i == y:
                if y in d and d[y] == 2:
                    return find(nums, y)
            else:
                if y in d and d[y] == 1:
                    return [find(nums, i)[0], find(nums, y)[0]]