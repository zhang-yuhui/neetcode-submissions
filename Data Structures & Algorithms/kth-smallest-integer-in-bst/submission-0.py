# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        tmp = 1
        def dfs(root):
            nonlocal tmp, ans
            if root.left is not None:
                dfs(root.left)
            
            if tmp == k:
                ans = root.val
            tmp += 1
            if root.right is not None:
                dfs(root.right)

        dfs(root)
        return ans
