# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        not root => -INF
        
        if root.val > 0
            max(root.val, root.val +pathleft, root.val +pathright)
        else:
            max(root.val, pathleft, pathright)
    
        only at most one node where both subtrees are taken
        dp_l[root]: max sum of stick on left sub tree
        dp_r[root]: max sum of stick on right sub tree
        for each root:
            if root.val > 0
                ans = max(ans, root.val, root.val +pathleft, root.val +pathright)
            else:
                ans = max(ans, root.val, pathleft, pathright)
        """
        stk = []
        # push to stack level by level
        def push_to_stack(root):
            if root is None:
                return
            stk.append(root)
            push_to_stack(root.left)
            push_to_stack(root.right)
        push_to_stack(root)
        dp_l = {}
        dp_r = {}
        INF = 1000000
        while len(stk) > 0:
            cur_node = stk.pop()
            if cur_node not in dp_l:
                dp_l[cur_node] = -INF
            if cur_node not in dp_r:
                dp_r[cur_node] = -INF
            if cur_node.left is not None:
                dp_l[cur_node] = cur_node.left.val + max(dp_l[cur_node.left], dp_r[cur_node.left], 0)
            else:
                dp_l[cur_node.left] = dp_r[cur_node.left] = -INF
            if cur_node.right is not None:
                dp_r[cur_node] = cur_node.right.val + max(dp_l[cur_node.right], dp_r[cur_node.right], 0)
            else:
                dp_r[cur_node.right] = dp_r[cur_node.right] = -INF
        ans = -INF
        for node in dp_l.keys():
            if node is not None:
                # print(node.val, dp_l[node], dp_r[node])
                ans = max(ans, node.val + max(dp_l[node], dp_r[node], 0, dp_l[node] + dp_r[node]))
        return ans
            