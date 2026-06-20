# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root, p):
            nonlocal ans
            if root.val >= p:
                ans += 1
                print(root.val)
            
            if root.left is not None:
                dfs(root.left, max(root.val, p))
            
            if root.right is not None:
                dfs(root.right, max(root.val, p))
        
        dfs(root, root.val)
        return ans