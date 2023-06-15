# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n: number of nodes in tree
        d = {} # level: sum
        def traverse(root, cur_level):
            if root is None:
                return
            if cur_level not in d:
                d[cur_level] = 0
            d[cur_level] += root.val
            traverse(root.left, cur_level+1)
            traverse(root.right, cur_level+1)
        traverse(root, 1)
        maxx = None
        max_level = None
        for k,v in d.items():
            if maxx is None or (v > maxx or (v == maxx and k < max_level)):
                maxx = v
                max_level = k
        return max_level