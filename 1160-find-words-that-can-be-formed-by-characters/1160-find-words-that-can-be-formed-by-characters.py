class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_freq = {}
        for c in chars:
            if c not in char_freq:
                char_freq[c] = 0
            char_freq[c] += 1
        
        ans =0 
        for w in words:
            clone_char_freq = char_freq.copy()
            formed = True
            for c in w:
                if c not in clone_char_freq:
                    formed = False
                    break
                clone_char_freq[c] -= 1
                if clone_char_freq[c] == 0:
                    del clone_char_freq[c]
            if formed:
                ans += len(w)
        return ans