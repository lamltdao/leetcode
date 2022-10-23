class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        group words of same length
        
        """
        d = {}
        for w in words:
            if len(w) not in d:
                d[len(w)] = []
            d[len(w)].append(w)
        dp = {} # word: longest chain up to word
        words = set(words)
        ans = 0
        for word_len in range(1, 17):
            if word_len not in d:
                continue
            for w in d[word_len]:
                dp[w] = 1
                for i in range(len(w)): # remove 1 char at idx i to make new word
                    new_w = w[:i] + w[i+1:]
                    if new_w in dp:
                        dp[w] = max(dp[w], dp[new_w]+1)
                ans = max(ans, dp[w])
        return ans
                        