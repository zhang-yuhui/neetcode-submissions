class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x, y, z = 0, 0, 0
        
        for i in num1:
            x *= 10
            x += ord(i) - ord('0')
        
        for i in num2:
            y *= 10
            y += ord(i) - ord('0')
        
        z = x * y

        ans = ""
        while z > 0:
            tmp = z % 10
            ans += chr(ord('0') + tmp)
            z = z // 10
        ans = ans[::-1]
        return ans if ans != "" else "0"