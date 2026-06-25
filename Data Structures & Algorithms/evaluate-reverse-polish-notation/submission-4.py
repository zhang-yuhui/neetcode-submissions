from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        q = deque()
        f = deque()
        sym = {'+', '-', "*", '/'}
        for s in tokens:
            q.append(s)
        while q:
            tmp = q.popleft()
            if tmp in sym:
                y = f.pop()
                x = f.pop()
                print(x, tmp, y)
                if tmp == '+':
                    x += y
                elif tmp == '-':
                    x -= y
                elif tmp == '*':
                    x *= y
                elif tmp == '/':
                    x = math.trunc(x / y)
                f.append(x)
            else:
                tmp = int(tmp)
                f.append(tmp)
        return f.pop()