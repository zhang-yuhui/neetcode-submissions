class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ele = dict()
        n = len(nums)
        for i in range(n):
            if nums[i] in ele:
                ele[nums[i]] += 1
            else:
                ele[nums[i]] = 1
        
        keys = list(ele.keys())
        ans = [[]]
        def dfs(x, ss, l):
            nonlocal ans, ele, keys
            if len(ss) == l:
                ans.append(ss.copy())
                return
            if x == len(keys):
                return
            
            k, v = keys[x], ele[keys[x]]

            for i in range( min(v, l-len(ss)) + 1):
                dfs(x+1, ss+([k]*i), l)
        
        for i in range(1, n+1):
            dfs(0, [], i)
        return ans