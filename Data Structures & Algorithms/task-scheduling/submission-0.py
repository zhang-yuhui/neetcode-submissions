class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = defaultdict(int)
        for i in tasks:
            t[i] += 1
        
        total = len(tasks)
        ans = 0
        pq = []
        for k in t.keys():
            heapq.heappush(pq, (0, -t[k], k))
        stmp = 0
        while pq:
            time, f, s = heapq.heappop(pq)
            f = -f
            f -= 1
            if time <= stmp:
                stmp += 1
            else:
                stmp += 1 + (time - stmp)
            if f > 0:
                time += n + 1
                heapq.heappush(pq, (time, -f, s))
        
        return stmp