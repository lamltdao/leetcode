class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0 for _ in range(n)]
        for i in range(n):
            scores[edges[i]] += i
        maxx = -1
        max_idx = None
        for i in range(n):
            if scores[i] > maxx:
                maxx = scores[i]
                max_idx = i
        return max_idx