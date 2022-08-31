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
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        heapify(pq)
        if a > 0:
            heappush(pq, Item('a', a))
        if b > 0:
            heappush(pq, Item('b', b))
        if c > 0:
            heappush(pq, Item('c', c))
        ans = ''
        while len(pq) > 0:
            item = heappop(pq)
            char, freq = item.char, item.freq
            # different char from the latest char added
            if len(ans) == 0 or ans[-1] != char:
                num_pop = min(2, freq)
                ans += char * num_pop
                if freq - num_pop > 0:
                    heappush(pq, Item(char, freq-num_pop))
            else: # ans[-1] == char
                # add one char of different char
                if len(pq) > 0:
                    i = heappop(pq)
                    c, f = i.char, i.freq
                    ans += c
                    f -= 1
                    if f > 0:
                        heappush(pq, Item(c,f))
                    # push the char with most occurrence back in pq, as it is not added this time
                    heappush(pq, Item(char, freq))
        return ans                    
                            
        