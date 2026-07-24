from _heapq import heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i in stones:
            heapq.heappush(pq, -i)
        while len(pq) > 1:
            x = heapq.heappop(pq) * -1
            y = heapq.heappop(pq) * -1
            if x == 0 and y == 0:
                return 0
            heapq.heappush(pq, -abs(x-y))
        return heapq.heappop(pq) * -1