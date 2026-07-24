class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        n = len(word)
        cur = self.tree
        for i in range(n):
            s = word[i]
            if s not in cur:
                cur[s] = {}
            cur = cur[s]
        cur['.'] = '.'

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(pos, tree):
            if pos == n:
                return '.' in tree
            if word[pos] != '.':
                if word[pos] in tree:
                    return dfs(pos+1, tree[word[pos]])
                else:
                    return False
            else:
                r = False
                for c in tree:
                    if c == '.':
                        continue
                    r = r or dfs(pos+1, tree[c])
                return r
        return dfs(0, self.tree)
