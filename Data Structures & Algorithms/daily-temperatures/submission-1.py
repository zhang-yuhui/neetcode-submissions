class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        ans = []
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            if not q or temperatures[i] >= q[-1][0]:
                while q and temperatures[i] >= q[-1][0]:
                    q.pop()
                if not q:
                    ans.append(0)
                else:
                    ans.append(q[-1][1]-i)
                q.append([temperatures[i],i])
                
            else:
                ans.append(q[-1][1]-i)
                q.append([temperatures[i],i])

        
        ans.reverse()
        return ans