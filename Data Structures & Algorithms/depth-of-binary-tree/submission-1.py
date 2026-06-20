# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 1
        def dfs(root, depth):
            nonlocal ans
            if root is None:
                return
            ans = max(ans, depth)

            if root.right:
                dfs(root.right, depth+1)
            if root.left:
                dfs(root.left, depth+1)
        dfs(root, 1)
        return ans