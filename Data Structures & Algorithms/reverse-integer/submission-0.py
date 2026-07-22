class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        neg = x < 0
        ans = 0
        if x > 0:
            x = -x
        while x != 0:
            r = 10 - (x%10) if x % 10 != 0 else 0
            x += r
            x = x // 10
            if ans == 0:
                ans = -abs(r)
            else:
                inf = -2**31 if neg else -2**31 -1
                if (inf + r) // 10 + 1 <= ans:
                    ans = ans *10 -r
                else:
                    return 0
            
        return ans if neg else -ans