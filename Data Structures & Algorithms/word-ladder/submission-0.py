from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bank = set(wordList)
        if endWord not in bank:
            return 0
        
        visited = set()
        q = deque()
        q.appendleft((beginWord,1))
        l = len(beginWord)

        while q:
            (s, step) = q.pop()
            visited.add(s)
            for i in range(len(s)):
                for j in range(26):
                    ns = s[:i] + chr(ord('a')+j) + s[i+1:]
                    if ns in bank and ns not in visited:
                        visited.add(ns)
                        q.appendleft((ns,step+1))
                        if ns == endWord:
                            return step+1
        
        return 0
            
