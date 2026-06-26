# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def fd(root:TreeNode, x, y):
            if root.val > x and root.val > y and root.left:
                return fd(root.left, x, y)
            if root.val < x and root.val < y and root.right:
                return fd(root.right, x, y)
            return root
        
        return fd(root, p.val, q.val)