import bisect
class TimeMap:

    def __init__(self):
        self.db = {}
        self.dbl = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = {}
            self.dbl[key] = []
        self.db[key][timestamp] = value
        self.dbl[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        idx = bisect.bisect_right(self.dbl[key], timestamp) - 1

        if idx < 0:
            return ""

        res = self.dbl[key][idx]
        return self.db[key][res]
