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
        """
        prioritize char with more occu

        avoid 3 consecutive chars by introducing var prev_char + prev_char_count + pop until new char + push back to pq
        """
        pq = []
        heapify(pq)
        if a > 0:
            heappush(pq, Item('a', a))
        if b > 0:
            heappush(pq, Item('b', b))
        if c > 0:
            heappush(pq, Item('c', c))
        prev_char = None
        prev_char_count = 0
        ans = ''
        while len(pq) > 0:
            item = heappop(pq)
            char, freq = item.char, item.freq
            if prev_char is None or prev_char != char:
                num_pop = min(2, freq)
                ans += char * num_pop
                prev_char = char
                prev_char_count = num_pop
                if freq - num_pop > 0:
                    heappush(pq, Item(char, freq-num_pop))
            else: # prev_char == char
                # add one char of different char
                if len(pq) > 0:
                    i = heappop(pq)
                    c, f = i.char, i.freq
                    ans += c
                    f -= 1
                    if f > 0:
                        heappush(pq, Item(c,f))
                    prev_char = c
                    prev_char_count = 1
                    heappush(pq, Item(char, freq))
        return ans                    
                            
        