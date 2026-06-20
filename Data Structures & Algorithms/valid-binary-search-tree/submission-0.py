# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkTree(root, mi, ma) -> bool:
            #print(root.val, mi, ma)
            if root.val >= ma or root.val <= mi:
                return False
            ans = True
            if root.left is not None:
                ans = ans and checkTree(root.left, mi, root.val)
            if root.right is not None:
                ans = ans and checkTree(root.right, root.val, ma)
            return ans

        return checkTree(root, -1001, 1001) 
        