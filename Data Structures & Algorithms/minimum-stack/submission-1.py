from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mi = deque()

    def push(self, val: int) -> None:
        if self.stack and self.mi[-1] < val:
            self.mi.append(self.mi[-1])
        else:
            self.mi.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.mi.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mi[-1]
