class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        p = (point[0], point[1])
        if p in self.points:
            self.points[p] += 1
        else:
            self.points[p] = 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        ans = 0
        for (px, py) in self.points:
            if px == x and py == y:
                continue
            if abs(px - x) == abs(py - y):
                if (px, y) in self.points and (x, py) in self.points:
                    ans += self.points[(px, y)] * self.points[(x, py)] * self.points[(px, py)]
        return ans

