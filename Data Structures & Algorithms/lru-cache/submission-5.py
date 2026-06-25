class LRUCache:
    class LinkList:
        def __init__(self, val, prev=None, nxt=None) -> None:
            self.val = val
            self.prev = prev
            self.nxt = nxt

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.s: dict = {}
        self.start = None
        self.end = None
    def get(self, key: int) -> int:
        if key in self.s:
            (val, node) = self.s[key]
            if self.end is not node:
                if node.prev is None:
                    self.start = node.nxt
                    node.nxt.prev = None
                else:
                    prev = node.prev
                    nxt = node.nxt
                    prev.nxt = nxt
                    nxt.prev = prev

                node.prev = self.end
                node.nxt = None
                self.end.nxt = node
                self.end = self.end.nxt
            #print(-2, self.start.val)
            return val
        else:
             return -1

    def put(self, key: int, value: int) -> None:
        if key in self.s:
            (val, node) = self.s[key]
            val = value
            if self.end.val != key:
                if node.prev is None:
                    self.start = node.nxt
                    node.nxt.prev = None
                else:
                    prev = node.prev
                    nxt = node.nxt
                    prev.nxt = nxt
                    nxt.prev = prev
                node.prev = self.end
                node.nxt = None
                self.end.nxt = node
                self.end = self.end.nxt
            self.s[key] = (value, node)
        else:
            node = self.LinkList(key)
            self.s[key] = (value, node)
            if self.start is not None:

                self.end.nxt = node
                node.prev = self.end
                self.end = self.end.nxt

            else:
                self.start = node
                self.end = node
            if len(self.s) > self.capacity:
                delkey = self.start.val
                v, delnode = self.s[delkey]
                self.start = self.start.nxt
                self.start.prev = None
                del delnode
                del self.s[delkey]
        #print(-1, self.start.val)


