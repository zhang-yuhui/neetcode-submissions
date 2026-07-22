class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ans = []
        ma = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        n = len(digits)
        def dfs(x, s):
            nonlocal ans, digits, ma
            if x == n:
                ans.append(s)
                return 
            cur = ma[digits[x]]
            for i in cur:
                dfs(x+1, s+i)
        dfs(0, "")
        return ans