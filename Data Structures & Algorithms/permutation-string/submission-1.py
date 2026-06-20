class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set_a = [0] * 26
        for i in s1:
            set_a[ord(i)-ord('a')] += 1
        print(set_a)
        n = len(s2)
        set_b = [0] * 26
        set_b[ord(s2[0]) - ord('a')] += 1
        for i in range(n):
            for j in range(i, n):
                ans = True
                for k in range(26):
                    if set_a[k] != set_b[k]:
                        ans = False
                        
                if ans:
                    return True
                if j != n - 1:
                    set_b[ord(s2[j + 1]) - ord('a')] += 1
                elif i != n - 1:
                    set_b = [0] * 26
                    set_b[ord(s2[i + 1]) - ord('a')] += 1
                else:
                    return False

        return False