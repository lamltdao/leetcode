class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        """
        abc
        b
        c
        """
        max_nrow = len(words)
        max_ncol = max([len(w) for w in words])
        for r in range(max_nrow):
            for c in range(max_ncol):
                has_char_1 = r < len(words) and c < len(words[r])
                has_char_2 = c < len(words) and r < len(words[c])
                if has_char_1 and has_char_2:
                    if words[r][c] != words[c][r]:
                        return False
                elif has_char_1 or has_char_2:
                    return False
        return True