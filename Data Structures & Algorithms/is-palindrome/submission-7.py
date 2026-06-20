class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        head, tail = 0, n-1
        def check(s):
            return ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9') 
        while head < tail:
            while head < n and not check(s[head]):
                head += 1
            while tail >= 0 and not check(s[tail]):
                tail -= 1
            if head >= tail:
                return True
            
            if s[head] != s[tail]:
                print(s[head], s[tail])
                return False
            else:
                head += 1
                tail -= 1
        
        return True