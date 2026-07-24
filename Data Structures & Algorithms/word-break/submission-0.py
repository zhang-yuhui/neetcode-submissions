class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        pos = []
        for i in range(n):
            pos.append([])
        
        l = len(wordDict)
        for i in range(l):
            for j in range(n - len(wordDict[i])+ 1):
                if s[j:j+len(wordDict[i])] == wordDict[i]:
                    pos[j+len(wordDict[i]) - 1].append(i)
        dp = [False] * n
        for i in range(n):
            for j in pos[i]:
                w = wordDict[j]
                if len(w) == i+1:
                    dp[i] = True
                else:
                    dp[i] = dp[i-len(w)] or dp[i] if i-len(w) >= 0 else False
        
        return dp[-1]

        