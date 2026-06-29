# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = ""

        def dfs(root):
            nonlocal ans
            if not root:
                # print(1, "none")
                ans += "None" + chr(0)
            else:
                ans += str(root.val) + chr(0)
                # print(1, root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        ans += chr(0)
        return ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ans = None
        idx = 0
        def dfs():
            nonlocal idx
            if idx < len(data) and data[idx] == chr(0):
                idx += 1
            if idx >= len(data):
                return None
            tmp = ""
            while data[idx] != chr(0):
                tmp += data[idx]
                idx += 1
            if tmp == "None":
                # print(2, "None")
                return None
            else:
                # print(2, tmp)
                tmp = int(tmp)
                idx += 1
                node = TreeNode(tmp)
                node.left = dfs()
                node.right = dfs()
                return node
        return dfs()





