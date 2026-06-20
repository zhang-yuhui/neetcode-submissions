# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(root):
            if root is None:
                return 

            if root.left is not None or root.right is not None:
                #print(root.val)
                tmp = root.left
                root.left = root.right
                root.right = tmp
            
            if root.left is not None:
                dfs(root.left)
            
            if root.right is not None:
                dfs(root.right)

        dfs(root)
        return root