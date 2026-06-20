# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            root.dpleft = 0
            root.dpright = 0
            
            if root.left is None and root.right is None:
                return

            if root.left is not None:
                dfs(root.left)
                root.dpleft = root.left.val + max(root.left.dpleft, root.left.dpright, 0)
            
            if root.right is not None:
                dfs(root.right)
                root.dpright = root.right.val + max(root.right.dpleft, root.right.dpright, 0)
                
            
        dfs(root)

        def findans(root):
            if root.left is None and root.right is None:
                return root.val
            ans = root.val
            if root.right is not None and root.dpright > 0:
                ans += root.dpright
            if root.left is not None and root.dpleft > 0:
                ans += root.dpleft
            
            if root.right is not None:
                ans = max(ans, findans(root.right))
            
            if root.left is not None:
                ans = max(ans, findans(root.left))
            
            return ans

        return findans(root)