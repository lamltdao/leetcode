class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        """
        abc
        b
        c
        """
        for w_idx, word in enumerate(words):
            for c_idx, char in enumerate(words[w_idx]):
                has_word_in_mirror_pos = c_idx < len(words) and w_idx < len(words[c_idx])
                if not has_word_in_mirror_pos or words[w_idx][c_idx] != words[c_idx][w_idx]:
                    return False
        return True
                