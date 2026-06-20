import heapq
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # rot = set()
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 2:
        #             rot.add((i, j))
        visited = set()

        maxtime = 0
        pq = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    pq.append((0, (i, j)))
                    visited.add((i, j))

        while len(pq) != 0:
            time, (i, j) = heapq.heappop(pq)
            maxtime = max(maxtime, time)
            for (pi, pj) in pos:
                ni, nj = i + pi, j + pj
                if ni >= 0 and ni < n and nj >= 0 and nj < m and (ni, nj) not in visited and grid[ni][nj] == 1:
                    visited.add((ni, nj))
                    heapq.heappush(pq, (time+1, (ni, nj)))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        
        return maxtime
           

                    
            
            
