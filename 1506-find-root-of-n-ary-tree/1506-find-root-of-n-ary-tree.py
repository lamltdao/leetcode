"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children_value_set = set()
        node_set = set()
        for t in tree:
            node_set.add(t)
            for c in t.children:
                children_value_set.add(c.val)
        for node in node_set:
            if node.val not in children_value_set:
                return node
        return None