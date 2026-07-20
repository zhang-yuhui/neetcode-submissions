class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        
        de = [0] * n

        for i in range(n):
            x1, x2, x3 = triplets[i]
            if x1 > target[0] or x2 > target[1] or x3 > target[2]:
                de[i] = 1
        ans = [-1, -1, -1]
        for i in range(n):
            if de[i] == 1:
                continue
            x1, x2, x3 = triplets[i]
            ans[0] = max(ans[0], x1)
            ans[1] = max(ans[1], x2)
            ans[2] = max(ans[2], x3)
        
        return ans[0]==target[0] and ans[1] == target[1] and ans[2] == target[2]