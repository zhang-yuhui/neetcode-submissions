from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        l = r = 0
        n = len(s)
        ans = 0
        while r != n:
            count[s[r]] += 1
            if count[s[r]] > 1:
                while s[l] != s[r]:
                    count[s[l]] -= 1
                    l += 1
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans