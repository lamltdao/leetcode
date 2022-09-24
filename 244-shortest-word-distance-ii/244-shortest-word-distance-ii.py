import bisect
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.map = {}
        for i in range(len(wordsDict)):
            w = wordsDict[i]
            if w not in self.map:
                self.map[w] = []
            self.map[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        pos_1 = self.map[word1]
        pos_2 = self.map[word2]
        # find n1, n2 in pos1, pos2 s.t abs(n1-n2) shortest. pos1 and pos2 are both sorted
        longer_len_arr = pos_1 if len(pos_1) >= len(pos_2) else pos_2
        shorter_len_arr = pos_1 if len(pos_1) < len(pos_2) else pos_2
        shortest_dist = 100000
        for num_s in shorter_len_arr:
            i = bisect.bisect_left(longer_len_arr, num_s)
            if i > 0:
                shortest_dist = min(shortest_dist, abs(num_s - longer_len_arr[i-1]))
            if i >= 0 and i < len(longer_len_arr):
                shortest_dist = min(shortest_dist, abs(num_s - longer_len_arr[i]))
            if i+1 < len(longer_len_arr):
                shortest_dist = min(shortest_dist, abs(num_s - longer_len_arr[i+1]))
        return shortest_dist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)