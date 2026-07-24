class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        n = len(nums)
        l = 0
        r = n-1
        while l < r:
            mid = (l+r) // 2
            if mid  == l:
                print(l, mid, r)
                return nums[r]
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[r]