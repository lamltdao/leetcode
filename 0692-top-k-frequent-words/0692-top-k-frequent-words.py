class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Time: O(nlogn), Space: O(#unique words) = O(n)
        f = {}
        for w in words:
            if w not in f:
                f[w] = 0
            f[w] += 1
        class Item:
            def __init__(self, word):
                self.word = word
            def __lt__(self, other):
                if f[self.word] != f[other.word]:
                    return f[self.word] > f[other.word]
                return self.word < other.word
        items = []
        for w in f.keys():
            items.append(Item(w))
        items.sort()
        ans = []
        for i in range(k):
            ans.append(items[i].word)
        return ans