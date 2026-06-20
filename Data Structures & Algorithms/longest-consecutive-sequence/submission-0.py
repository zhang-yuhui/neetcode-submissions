class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        ans = 0

        while len(s) > 0:
            
            mi = s.pop()
            ma = mi
            
            while (mi - 1) in s:
                s.remove(mi - 1)
                mi -= 1
            
            while (ma + 1) in s:
                s.remove(ma + 1)
                ma += 1
            ans = max(ans, (ma - mi + 1))
        return ans
        