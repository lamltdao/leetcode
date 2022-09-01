# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, ans, curMax):
        if root is None:
            return
        if curMax <= root.val:
            ans[0] += 1
            curMax = root.val
        self.dfs(root.left, ans, curMax)
        self.dfs(root.right, ans, curMax)
            
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = [0]
        self.dfs(root, ans, root.val)
        return ans[0]