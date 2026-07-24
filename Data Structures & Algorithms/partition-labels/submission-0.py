class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        f = {}
        pos = {}
        n = len(s)
        for i in range(n):
            x = s[i]
            if x in f:
                f[x] += 1
                pos[x].append(i)
            else:
                f[x] = 1
                pos[x] = [i]
        
        ans = []
        l, r = -1, -1
        for i in range(n):
            x = s[i]
            if f[x] == 1:
                if l == -1:
                    ans.append(1)
            else:
                if l == -1:
                    l = i
                    r = pos[x][-1]
                else:
                    r = max(r, pos[x][-1])
            if r == i:
                ans.append(r - l +1)
                l = r = -1
        return ans