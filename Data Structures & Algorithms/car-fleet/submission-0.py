class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = []
        n = len(position)
        for i in range(n):
            a.append((position[i], speed[i]))
        
        a.sort(reverse=True)
        ans = 0
        mint = -1
        for i in range(n):
            p, s = a[i]
            t = (target-p) / s
            if mint < t:
                mint = t
                ans += 1
                
        return ans