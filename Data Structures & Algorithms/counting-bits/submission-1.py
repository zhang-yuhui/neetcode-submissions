class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        if n == 0:
            return ans
        ans[1] = 1
        s = 2
        while s <= n:
            for i in range(s, min(n+1, s*2)):
                ans[i] = ans[i-s] + 1
            s *= 2
        return ans
