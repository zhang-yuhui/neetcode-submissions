class Solution:
    def trap(self, height: List[int]) -> int:
        height.insert(0, 0)
        height.append(0)
        high1 = 0
        low = 0
        high2 = -1
        n = len(height)

        ma = [height[-1]]
        for i in range(n - 2, -1, -1):
            ma.append(max(height[i], ma[-1]))
        ma.reverse()
        print(ma)
        ans = 0
        for i in range(1, n):
            if ma[i] == height[i] or height[high1] <= height[i]:
                h = min(height[high1], height[i])
                for j in range(high1, i + 1):
                    ans += max(0, h - height[j])
                print(i, high1, ans)
                high1 = i
                

        return ans
                    