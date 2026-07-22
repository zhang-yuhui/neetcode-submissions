class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        for i in range(k+1):
            tmp = dist.copy()
            for fl in flights:
                f, t, w = fl[0], fl[1], fl[2]
                if dist[f] != float('inf') and tmp[t] > dist[f] + w:
                    tmp[t] = dist[f] + w
            dist = tmp
        return dist[dst] if dist[dst] != float('inf') else -1