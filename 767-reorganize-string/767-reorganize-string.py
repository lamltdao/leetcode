from heapq import heapify, heappush, heappop

class Item:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        else:
            return self.char > other.char
class Solution:
    def reorganizeString(self, s: str) -> str:
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
            char, freq = item.char, item.freq
            if len(ans) == 0 or ans[-1] != char:
                ans += char
                freq -= 1
                if freq > 0:
                    heappush(pq, Item(char, freq))
            else:
                if len(pq) > 0:
                    i = heappop(pq)
                    c, f = i.char, i.freq
                    ans += c
                    f -= 1
                    if f > 0:
                        heappush(pq, Item(c,f))
                    heappush(pq, item)
                else:
                    return ''
        return ans