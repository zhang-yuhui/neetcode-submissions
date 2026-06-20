class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(level: int, cur: str, cnt: int) -> None:
            if len(cur) == level * 2:
                ans.append(cur)
                return
            front = cnt
            back = len(cur) - cnt
            if front > back: #put front or back
                if front < level:
                    dfs(level, cur+"(", cnt + 1)
                dfs(level, cur+")", cnt)
            
            if front == back:
                if front < level:
                    dfs(level, cur+"(", cnt + 1)
        
        dfs(n, "", 0)
        return ans