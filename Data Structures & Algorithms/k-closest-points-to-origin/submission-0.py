class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            d = math.sqrt(x*x + y*y)
            heapq.heappush(pq, (-d, [x, y]))
            if len(pq) > k:
                z = heapq.heappop(pq)
        
        return [i[1] for i in pq]