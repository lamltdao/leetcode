class Solution:
    def minDeletions(self, s: str) -> int:
        """
        abbcccddd => 3
        
        - store freqs in dict
        freqs[i] = true if there is char with freq i, i > 0
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        freqs = [[] for _ in range(len(s)+1)]
        for c in d.keys():
            freqs[d[c]].append(c)
        ans = 0
        for i in range(len(freqs)-1, 0, -1):
            if len(freqs[i]) > 1:
                num_type_reduced = len(freqs[i]) - 1
                num_char_reduced = 0
                for j in range(i-1, 0, -1):
                    if num_type_reduced == 0:
                        break
                    if len(freqs[j]) == 0:
                        freqs[j].append('\0')
                        num_type_reduced -= 1
                        num_char_reduced += i - j
                if num_type_reduced > 0: # delete all occurrences of chars
                    num_char_reduced += num_type_reduced * i
                ans += num_char_reduced
        return ans