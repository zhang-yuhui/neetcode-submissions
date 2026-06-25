class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        seg = [0] * (n * 4)
        def add(pos: int, val: int, start: int, end: int, cur):
            nonlocal seg
            if start == end:
                seg[cur] = val
                return
            mid = (start + end) // 2
            if pos <= mid:
                add(pos, val, start, mid, cur*2)
            else:
                add(pos, val, mid + 1, end, cur*2 + 1)
            seg[cur] = max(seg[cur*2], seg[cur*2+1])
        
        def fd(low, high, start, end, cur):
            nonlocal seg
            if low == start and high == end:
                return seg[cur]
            mid = (start + end) // 2
            if mid < low:
                return fd(low, high, mid + 1, end, cur*2+1)
            elif mid >= high:
                return fd(low, high, start, mid, cur*2)
            else:
                l = fd(low, mid, start, mid, cur*2)
                r = fd(mid+1, high, mid+1, end, cur*2+1)
                return max(l, r)

        for i in range(n):
            add(i, nums[i], 0, n-1, 1)
        
        start, end = 0, k-1
        ans = []
        while end < n:
            ans.append(fd(start, end, 0, n-1, 1))
            start += 1
            end += 1
        return ans
        

