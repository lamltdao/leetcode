class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        m = {}
        for i,c in enumerate(keyboard):
            m[c] = i
        last = 0
        ans = 0
        for w in word:
            ans += abs(m[w] - last)
            last = m[w]
        return ans