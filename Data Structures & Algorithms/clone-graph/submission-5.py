"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        ansl = []
        edges = set()
        n = 1
        visited = set()
        def dfs(node):
            nonlocal edges, n, visited
            if not node or node.val in visited:
                return
            f = node.val
            visited.add(f)
            for t in node.neighbors:
                v = t.val
                n = max(n, v, f)
                edges.add((f, v))
                edges.add((v, f))
            for t in node.neighbors:
                if t.val not in visited:
                    dfs(t)
        dfs(node)
        for i in range(n+1):
            ansl.append(Node(val=i))
        for f, t in edges:
            fn = ansl[f]
            tn = ansl[t]
            
            fn.neighbors.append(tn)
        return ansl[node.val]

