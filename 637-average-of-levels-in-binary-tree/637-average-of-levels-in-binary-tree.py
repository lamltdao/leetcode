# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        layers = {}
        q = deque()
        q.append((root, 0))
        layers[0] = [root.val]
        while len(q) > 0:
            node, layer = q.popleft()
            if layer not in layers:
                layers[layer] = []
            layers[layer].append(node.val)
            if node.left is not None:
                q.append((node.left, layer+1))
            if node.right is not None:
                q.append((node.right, layer+1))
        ans = [None for _ in range(len(layers))]
        for l in layers.keys():
            ans[l] = sum(layers[l]) / len(layers[l])
        return ans