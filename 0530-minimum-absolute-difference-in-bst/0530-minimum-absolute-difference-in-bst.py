# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        def inorder(root):
            nonlocal vals
            if root is None:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        inorder(root)
        vals.sort()
        ans = 10**5
        for i in range(len(vals)-1):
            ans = min(ans, vals[i+1] - vals[i])
        return ans
