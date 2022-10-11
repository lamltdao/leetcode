"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned = {}
        def helper(node):
            if node is None:
                return None
            if node.val in cloned:
                return cloned[node.val]
            new_node = Node(node.val)
            cloned[node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(helper(neighbor))
            return new_node
        return helper(node)