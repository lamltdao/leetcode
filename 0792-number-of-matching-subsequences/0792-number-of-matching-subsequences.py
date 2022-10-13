class Node:
    def __init__(self):
        self.children = {}
        self.is_end = 0
    def insert(self, word):
        tmp = self
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = Node()
            tmp = tmp.children[c]
        tmp.is_end += 1
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        trie out of words
        a-c-d
            \e
        b-b
        """
        ans = 0
        trie = Node()
        for w in words:
            trie.insert(w)
        def bt(cur_idx, cur_node):
            nonlocal ans, s
            if cur_node.is_end > 0:
                ans += cur_node.is_end
            for c in cur_node.children:
                matched_idx = cur_idx
                while matched_idx < len(s) and s[matched_idx] != c:
                    matched_idx += 1
                if matched_idx < len(s):
                    bt(matched_idx+1, cur_node.children[c])
        bt(0, trie)
        return ans