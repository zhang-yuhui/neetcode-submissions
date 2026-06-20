# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        dep = -1

        def dfs(root, d):
            nonlocal ans, dep
            if root is None:
                return
            if d > dep:
                ans.append(root.val)
                dep  = d
            
            if root.right is not None:
                dfs(root.right, d + 1)
            if root.left is not None:
                dfs(root.left, d + 1)
        dfs(root, 0)
        return ans