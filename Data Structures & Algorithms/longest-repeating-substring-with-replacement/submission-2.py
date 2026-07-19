class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        
        count = {}
        l, r = 0, 0
        for i in range(26):
            count[chr(ord('A') + i)] = 0
        ans = 0
        while r != n:
            count[s[r]] += 1
            maxf = max(count.values())
            while r - l + 1 - maxf > k:
                
                count[s[l]] -= 1
                l += 1
                maxf = max(count.values())
            
            ans = max(ans, r - l + 1)
            # print(r, l, ans)
            r += 1
        return ans
            
