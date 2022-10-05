# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        # go to nodes at depth-1
        def dfs(root, cur_depth):
            nonlocal depth
            if root is None:
                return
            if cur_depth == depth-1:
                tmp_left = root.left
                tmp_right = root.right
                root.left = TreeNode(val)
                root.left.left = tmp_left
                root.right = TreeNode(val)
                root.right.right = tmp_right
                return
            dfs(root.left, cur_depth+1)
            dfs(root.right, cur_depth+1)
        dfs(root, 1)
        return root