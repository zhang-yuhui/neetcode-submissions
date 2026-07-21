class PrefixTree:

    def __init__(self):
        self.trie = {'#': {}}

    def insert(self, word: str) -> None:
        l = len(word)
        cur = self.trie
        for i in range(l):
            if word[i] in cur:
                cur = cur[word[i]]
            else:
                cur[word[i]] = {}
                cur = cur[word[i]]
        cur['#'] = {}


    def search(self, word: str) -> bool:
        l = len(word)
        cur = self.trie
        for i in range(l):
            if word[i] not in cur:
                return False
            cur = cur[word[i]]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        cur = self.trie
        for i in range(l):
            if prefix[i] not in cur:
                return False
            cur = cur[prefix[i]]
        return True
        