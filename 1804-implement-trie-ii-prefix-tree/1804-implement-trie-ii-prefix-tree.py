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
    def erase(self, word):
        tmp = self
        for c in word:
            tmp = tmp.children[c]
        tmp.is_end -= 1
class Trie:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        self.trie.insert(word)

    def countWordsEqualTo(self, word: str) -> int:
        tmp = self.trie
        for c in word:
            if c not in tmp.children:
                return 0
            tmp = tmp.children[c]
        return tmp.is_end

    def countWordsStartingWith(self, prefix: str) -> int:
        tmp = self.trie
        for c in prefix:
            if c not in tmp.children:
                return 0
            tmp = tmp.children[c]
        ans = 0
        def bt(cur_node):
            nonlocal ans
            if cur_node.is_end > 0:
                ans += cur_node.is_end
            for c in cur_node.children:
                bt(cur_node.children[c])
        bt(tmp)
        return ans
    def erase(self, word: str) -> None:
        self.trie.erase(word)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)