class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def cal(x):
            ans = 0
            while x > 0:
                ans += (x % 10)**2
                x //= 10
            return ans
        while True:
            if n == 1:
                return True
            elif n in s:
                return False
            else:
                
                s.add(n)
                n = cal(n)