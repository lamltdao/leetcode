# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        helper(root)
            find min, max in root.left and root.right
        """
        def helper(root) -> tuple[int]:
            nonlocal ans
            if root is None:
                return (None, None)
            min_l, max_l = helper(root.left)
            min_r, max_r = helper(root.right)
            minn = maxx = root.val
            if min_l is not None and max_l is not None:
                ans = max(ans, abs(root.val - min_l), abs(root.val - max_l))
                minn = min(minn, min_l)
                maxx = max(maxx, max_l)
            if min_r is not None and max_r is not None:
                ans = max(ans, abs(root.val - min_r), abs(root.val - max_r))
                minn = min(minn, min_r)
                maxx = max(maxx, max_r)
            return (minn, maxx)
        ans = 0
        helper(root)
        return ans