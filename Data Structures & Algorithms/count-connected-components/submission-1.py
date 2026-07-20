class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]

        def find(x):
            nonlocal parent
            if parent[x] == x:
                return x
            p = find(parent[x])

            parent[x] = p
            return p 
        
        for e in edges:
            f, t = e[0], e[1]
            pf = find(f)
            pt = find(t)
            if pf != pt:
                parent[pf] = pt
        s = set()
        for i in range(n):
            s.add(find(i))
        return len(s)