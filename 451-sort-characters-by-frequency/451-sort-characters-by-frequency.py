from heapq import heapify, heappush, heappop

class Item:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        return self.val < other.val
class Solution:
    def frequencySort(self, s: str) -> str:
        pq = []
        heapify(pq)
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        for c in d.keys():
            heappush(pq, Item(c, d[c]))
        ans = ''
        while len(pq) > 0:
            item = heappop(pq)
            v, f = item.val, item.freq
            ans += v * f
        return ans