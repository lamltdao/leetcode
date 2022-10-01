# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        # return [true, true] if root or one of its children has p and q as descendants
        def dfs(root):
            nonlocal lca,p,q
            if root is None:
                return [False, False]
            ans = [False, False]
            if root.val == p.val:
                ans[0] = True
            if root.val == q.val:
                ans[1] = True
            ans_l = dfs(root.left)
            ans_r = dfs(root.right)
            ans[0] = ans[0] or ans_l[0] or ans_r[0]
            ans[1] = ans[1] or ans_l[1] or ans_r[1]
            if ans[0] and ans[1] and lca is None:
                lca = root
            return ans
        dfs(root)
        return lca