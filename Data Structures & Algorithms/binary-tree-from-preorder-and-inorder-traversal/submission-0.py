# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = dict()
        n = len(preorder)
        for i in range(n):
            d[inorder[i]] = i
        idx = 0
        def build(start, end):
            nonlocal idx
            if idx >= n:
                return None
            if preorder[idx] not in d:
                return None
            mid = d[preorder[idx]]
            val = preorder[idx]
            print(val, idx)
            node = TreeNode(val)
            if mid != start:
                idx += 1
                node.left = build(start, mid - 1)
            else:
                node.left = None
            if mid != end:
                idx += 1
                node.right = build(mid + 1, end)
            else:
                node.right = None
            return node
        
        return build(0, n-1)
