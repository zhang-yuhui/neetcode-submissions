import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge = {}
        
        for e in times:
            f, t, w = e[0], e[1], e[2]
            if f in edge:
                edge[f].append((t, w))
            else:
                edge[f] = [(t, w)]
        
        pq = []
        if k not in edge:
            return -1
        for t, w in edge[k]:
            heapq.heappush(pq, (w, t))
        # if len(edge) != n:
        #     print(1)
        #     return -1
        res = {k:0}
        visited = set()
        visited.add(k)
        while pq:
            w, t = heapq.heappop(pq)
            
            if t in visited:      # ← already settled with shortest path
                continue
            visited.add(t)
            res[t] = w            # ← ONLY set here, guaranteed shortest

            if t not in edge:
                continue
            for nt, nw in edge[t]:
                if nt not in visited:
                    heapq.heappush(pq, (w + nw, nt))
        ans = -1

        for i in range(1, n+1):
            if i not in res:
                return -1
            ans = max(ans, res[i])
        return ans
        
