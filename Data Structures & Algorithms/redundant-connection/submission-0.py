class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n + 1))
        def find(x):
            nonlocal parent
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for i in edges:
            x, y = i[0], i[1]

            p1, p2 = find(x), find(y)
            if p1 == p2:
                return [x, y]
            else:
                parent[p1] = p2
        
        return [-1, -1]