class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        parent = list(range(n))
        def find(x):
            if parent[x] == x:
                return x
            p = find(parent[x])
            parent[x] = p
            return p
        for e in edges:
            f, t = e[0], e[1]
            pf, pt = find(f), find(t)
            if pf == pt:
                return False
            else:
                parent[pf] = pt
                visited.add(f)
                visited.add(t)
        p = find(0)
        for i in range(1, n):
            if p != find(i):
                return False
        return True
        