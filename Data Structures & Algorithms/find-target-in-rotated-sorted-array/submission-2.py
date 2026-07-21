
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums[0] < nums[-1]:
            ans = bisect_left(nums, target) 
            return ans if ans < n and nums[ans] == target else -1 

        
        l, r = 0, n-1
       
        p = 0
        while l <= r:
            mid = (l+r) // 2

            if mid == l:
                p = l
                break
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid
        print(p)
        if target >= nums[0]:
            ans =  bisect_left(nums[:p], target) 
            return ans if nums[ans] == target else -1
        else:
            ans =  bisect_left(nums[p+1:], target) + p + 1
            return ans if ans < n and nums[ans] == target else -1
