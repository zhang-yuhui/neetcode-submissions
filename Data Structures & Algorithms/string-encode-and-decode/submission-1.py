class Solution:
    
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            n = len(i)
            s = s + str(n) + '#'
            s = s + i
        return s
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        l = ""
        ans = []
        while i < n:
            if s[i] != '#':
                l += s[i]
                i += 1
            else:
                le = int(l)
                i+= 1
                ans.append(s[i:i+le])
                i += le
                l = ""
        return ans
            


