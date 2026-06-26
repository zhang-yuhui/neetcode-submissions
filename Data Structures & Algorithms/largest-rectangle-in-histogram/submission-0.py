from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        n = len(heights)
        l = []
        r = []
        for i in range(n):
            if len(stack) == 0 or stack[-1][0] < heights[i]:
                l.append(i)
                stack.append((heights[i], i))
            else:
                while stack and stack[-1][0] >= heights[i]:
                    x = stack.pop()
                    print(x, i)
                if not stack:
                    l.append(0)
                else:
                    l.append(stack[-1][1]+1)
                stack.append((heights[i], i))
        
        stack.clear()
        for i in range(n-1, -1, -1):
            if len(stack) == 0 or stack[-1][0] < heights[i]:
                r.append(i)
                stack.append((heights[i], i))
            else:
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                if not stack:
                    r.append(n-1)
                else:
                    r.append(stack[-1][1]-1)
                stack.append((heights[i], i))
        r.reverse()
        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (r[i] - l[i] + 1))

        return ans