class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        ans = []
        
        def dfs(length, rest: Set[int], cur: List[int])-> None:
            if len(cur) == length:
                ans.append(cur.copy())
                return
            
            for i in list(rest):
                rest.remove(i)
                cur.append(i)
                dfs(length, rest, cur)
                cur.pop()
                rest.add(i)
            
        dfs(n, set(nums), [])
        return ans