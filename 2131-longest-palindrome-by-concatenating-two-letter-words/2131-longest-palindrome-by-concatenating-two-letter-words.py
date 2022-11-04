class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        word length is 2
        ab ba
        
        number of pairs * 2 + number of word with same chars
        
        """
        d = {}
        palin_words = {}
        for w in words:
            if w[0] == w[1]:
                if w not in palin_words:
                    palin_words[w] = 0
                palin_words[w] += 1
            else:
                sorted_w = ''.join(sorted(w))
                if sorted_w not in d:
                    d[sorted_w] = [0,0]
                if w == sorted_w:
                    d[sorted_w][0] += 1
                else:
                    d[sorted_w][1] += 1
        ans = 0
        for w in palin_words.keys():
            if palin_words[w] >= 2:
                ans += palin_words[w] // 2 * 4
                palin_words[w] %= 2
        if any(palin_words.values()):
            ans += 2
        for w in d.keys():
            ans += min(d[w]) * 4
        return ans
                    
                