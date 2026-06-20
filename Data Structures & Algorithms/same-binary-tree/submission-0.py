# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(r1, r2):
            nonlocal ans
            r1n = r1 is None
            r2n = r2 is None
            if (r1n ^ r2n) == True or (r1 and r2 and r1.val!=r2.val):
                ans = False
                return
            if not (r1 and r2):
                return
            dfs(r1.left, r2.left)
            dfs(r1.right, r2.right)
        dfs(p, q)
        return ans

