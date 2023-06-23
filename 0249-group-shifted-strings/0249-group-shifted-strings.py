class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = {}
        # if num < 0 => shift left
        def shift_right(char, num):
            return chr((ord(char) - ord('a') + num) % 26 + ord('a'))
        m = {}
        for w in strings:
            shifted_w = []
            num_shift = ord('a') - ord(w[0])
            for c in w:
                shifted_w.append(shift_right(c, num_shift))
            shifted_w = ''.join(shifted_w)
            if shifted_w not in m:
                m[shifted_w] = []
            m[shifted_w].append(w)
        return m.values()