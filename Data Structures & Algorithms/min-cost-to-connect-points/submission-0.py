from abc import abstractproperty
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edge = []
        for i in range(n):
            edge.append([0] * n)
        for i in range(n-1):
            for j in range(i, n):
                x = points[i]
                y = points[j]
                dis = abs(x[1] - y[1]) + abs(x[0] - y[0])
                edge[i][j] = dis
                edge[j][i] = dis
        
        ans = 0

        pq = [(0, 0, -1)]
        visited = set()
        while len(pq) > 0 and len(visited) < n:
            (w, start, parient) = heapq.heappop(pq)
            if start in visited:
                continue
            
            visited.add(start)

            ans += w
            for i in range(n):
                if i not in visited:
                    heapq.heappush(pq, (edge[start][i], i, start))

        return ans
